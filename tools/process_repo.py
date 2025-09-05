import importlib.util
import inspect
import logging
import os
import sys
import typing
from collections.abc import GenericAlias
from inspect import Parameter
from pathlib import Path
from typing import _TypedDictMeta, _UnionGenericAlias, _AnyMeta, ForwardRef

logging.basicConfig(level=logging.INFO)

mathesar_path = Path(sys.argv[1]).resolve()
sys.path.insert(0, str(mathesar_path))
os.chdir(mathesar_path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.production")
from django.core.management import execute_from_command_line
execute_from_command_line(["help"])
from django.conf import settings

members = []
for rpc_name in settings.MODERNRPC_METHODS_MODULES:
    rpc_path = mathesar_path / rpc_name.replace(".", os.path.sep)
    if rpc_path.exists():
        if rpc_path.is_dir():
            rpc_path = rpc_path / "__init__.py"
        else:
            raise RuntimeError
    else:
        rpc_path = str(rpc_path) + ".py"
    spec = importlib.util.spec_from_file_location(rpc_name, rpc_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[rpc_name] = module
    try:
        spec.loader.exec_module(module)
    except FileNotFoundError as exc:
        logging.exception(exc)
        continue
    for name, member in inspect.getmembers(module):
        if getattr(member, "modernrpc_enabled", False):
            members.append(member)


parsed_classes = {}
def parse_annotation(ann, use_not_required):
    if isinstance(ann, _TypedDictMeta):
        cls_name = str(ann).split("'")[1].split(".")[-1]
        if cls_name not in parsed_classes:
            parsed_classes[cls_name] = {
                "name": cls_name,
                "doc": ann.__doc__,
                "params": [
                    {
                        "name": n,
                        "type": parse_annotation(p, True)
                    }
                    for n, p in ann.__annotations__.items()
                ]
            }
        return cls_name
    elif isinstance(ann, typing._LiteralGenericAlias):
        args = typing.get_args(ann)
        return f"Literal[{", ".join(f"'{a}'" for a in args)}]"
    elif isinstance(ann, GenericAlias):
        orig = typing.get_origin(ann)
        args = typing.get_args(ann)
        if orig == list:
            return f"list[{parse_annotation(args[0], use_not_required)}]"
        elif orig == dict:
            return f"dict[{parse_annotation(args[0], use_not_required)}, {parse_annotation(args[1], use_not_required)}]"
        else:
            raise NotImplementedError
    elif isinstance(ann, _UnionGenericAlias):
        args = typing.get_args(ann)
        if len(args) == 2 and args[1] == type(None):
            if use_not_required:
                return f"NotRequired[{parse_annotation(args[0], use_not_required)}]"
            else:
                return f"Optional[{parse_annotation(args[0], use_not_required)}]"
        else:
            return f"Union[{", ".join([
                parse_annotation(a, use_not_required)
                for a in args
            ])}]"
    elif isinstance(ann, _AnyMeta):
        return "Any"
    elif isinstance(ann, ForwardRef):
        return f"'{ann.__forward_arg__}'"
    elif ann is None:
        return "None"
    else:
        return str(ann).split("'")[1]

parsed_methods = []
for method in members:
    sig = inspect.signature(method)
    parsed_methods.append({
        "name": method.modernrpc_name,
        "doc": method.__doc__,
        "params": [
            {
                "name": param.name
            } | ({
                "type": parse_annotation(param.annotation, False),
            } if param.annotation is not Parameter.empty else {}) | ({
                "default": param.default
            } if param.default is not Parameter.empty else {

            })
            for param in sig.parameters.values()
            if param.name not in ("args", "kwargs")
        ],
        "return": {
            "type": parse_annotation(sig.return_annotation, False)
        } if sig.return_annotation is not Parameter.empty else {}
    })


def tab(string: str):
    return "\n".join([
        f"    {line}"
        for line in string.splitlines()
    ])


def parse_method(meth):
    meth_name = meth["name"].replace(".", "_")
    params = []
    params_with_default = []
    for param in meth["params"]:
        default = param.get("default", Parameter.empty)
        if isinstance(default, list):
            default = tuple(default)
        if default is Parameter.empty:
            params.append(f"{param["name"]}: {param["type"]}")
        else:
            f"{param["name"]}: {param["type"]} = {default}"
    params.extend(params_with_default)
    if len(params) == 0:
        params = ["self", "**kwargs"]
    else:
        params = ["self", "/", *params, "**kwargs"]
    params_str = ", ".join(params)
    if meth["return"].get("type", "None") != "None":
        return_str = f" -> {meth["return"]["type"]}"
    else:
        return_str = ""
    return f"""@api("{meth["name"]}")
def {meth_name}({params_str}){return_str}:
    \"\"\"""" + tab(meth["doc"]) + """
    \"\"\"
    
    ...
"""

out_path = Path(__file__).parent.parent / "src" / "commonspider_mathesarpy"
with open(out_path / "api.py", "w") as f:
    f.write(
"""from typing import Literal, Optional

from .classes import *
from .client import Client, api


class API(Client):
""" + tab("\n".join(
    parse_method(p_method)
    for p_method in parsed_methods
)) + "\n"
    )


def parse_class(cls):
    return f"class {cls["name"]}(TypedDict):\n" + "\n".join([
        f"    {param["name"]}: {param["type"]}"
        for param in cls["params"]
    ]) + "\n"


with open(out_path / "classes.py", "w") as f:
    f.write(
"""from typing import TypedDict, Union, Any, NotRequired, Literal


""" + "\n\n".join([
    parse_class(p)
    for _, p in parsed_classes.items()
])
    )
