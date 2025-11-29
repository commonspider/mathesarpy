import importlib.util
import inspect
import logging
import os
import sys
import types
import typing
from inspect import Parameter
from pathlib import Path

none_type = type(None)

logging.basicConfig(level=logging.INFO)

output_path = Path(__file__).parent.parent / "src" / "commonspider_mathesarpy"

mathesar_path = Path(sys.argv[1]).resolve()
sys.path.insert(0, str(mathesar_path))

tools_path = Path("tools")
with open(tools_path / "settings_base.py") as f:
    data = f.read()
data = data.format(base_dir=mathesar_path)
with open(tools_path / "settings.py", "w") as f:
    f.write(data)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tools.settings")
from django.core.management import execute_from_command_line
execute_from_command_line(["help"])
from django.conf import settings

methods = []
for rpc_name in settings.MODERNRPC_METHODS_MODULES:
    rpc_path = mathesar_path / rpc_name.replace(".", os.path.sep)
    if rpc_path.is_dir():
        rpc_path = rpc_path / "__init__.py"
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
            methods.append(member)

parsed_classes = {}


def parse_annotation(ann, use_not_required=False):
    if isinstance(ann, typing._TypedDictMeta):
        cls_name = ann.__name__
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
    elif isinstance(ann, type):
        return ann.__name__
    elif isinstance(ann, typing._LiteralGenericAlias):
        args = typing.get_args(ann)
        return f"Literal[{", ".join(f"'{a}'" for a in args)}]"
    elif isinstance(ann, types.GenericAlias):
        orig = typing.get_origin(ann)
        args = typing.get_args(ann)
        if orig == list:
            return f"list[{parse_annotation(args[0])}]"
        elif orig == dict:
            return f"dict[{parse_annotation(args[0])}, {parse_annotation(args[1])}]"
    elif isinstance(ann, typing._UnionGenericAlias):
        args = list(typing.get_args(ann))
        if type(None) in args:
            args.remove(type(None))
        joined = ", ".join([
            parse_annotation(a)
            for a in args
        ])
        if len(args) == 1:
            if use_not_required:
                return f"NotRequired[{joined}]"
            else:
                return f"Optional[{joined}]"
        else:
            return f"Union[{joined}]"
    elif isinstance(ann, typing._AnyMeta):
        return "Any"
    elif isinstance(ann, str):
        return f"'{ann}'"
    elif isinstance(ann, typing.ForwardRef):
        return f"'{ann.__forward_arg__}'"
    raise TypeError


def parse_parameter(parameter: Parameter):
    parsed = {
        "name": parameter.name
    }
    if parameter.annotation is not Parameter.empty:
        parsed["type"] = parse_annotation(parameter.annotation)
    if parameter.default is not Parameter.empty:
        parsed["default"] = parameter.default
    return parsed


parsed_methods = []
for method in methods:
    signature = inspect.signature(method)
    parsed_method = {
        "name": method.modernrpc_name,
        "doc": method.__doc__,
        "params": [
            parse_parameter(param)
            for param in signature.parameters.values()
            if param.name not in ("args", "kwargs")
        ],
    }
    if signature.return_annotation not in (Parameter.empty, None):
        parsed_method["return"] = parse_annotation(signature.return_annotation)
    parsed_methods.append(parsed_method)


def tab(string: str):
    return "\n".join([
        f"    {line}"
        for line in string.splitlines()
    ])


def format_method(meth):
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
            params_with_default.append(f"{param["name"]}: {param["type"]} = {default}")
    params.extend(params_with_default)
    if len(params) == 0:
        params = ["self", "**kwargs"]
    else:
        params = ["self", "/", *params, "**kwargs"]
    params_str = ", ".join(params)
    if "return" in meth:
        return_str = f" -> {meth["return"]}"
    else:
        return_str = ""
    return f"""@api("{meth["name"]}")
def {meth_name}({params_str}){return_str}:
    \"\"\"""" + tab(meth["doc"]) + """
    \"\"\"
"""


with open(output_path / "api.py", "w") as f:
    f.write(
        """from typing import Optional
        
from .classes import *
from .client import Client, api


class API(Client):
""" + tab("\n".join(
    format_method(p_method)
    for p_method in parsed_methods
)) + "\n")


def parse_class(cls):
    return (
            f"class {cls["name"]}(TypedDict):\n" +
            '    """' +
            tab(cls["doc"]) +
            '\n    """\n\n' +
            "\n".join([
                f"    {param["name"]}: {param["type"]}"
                for param in cls["params"]
            ]) + "\n"
    )


with open(output_path / "classes.py", "w") as f:
    f.write(
        """from typing import TypedDict, Union, Any, NotRequired, Literal


""" + "\n\n".join([
    parse_class(p)
    for _, p in parsed_classes.items()
]))
