import json
from pathlib import Path
from typing import TypedDict, Optional, Literal, Union, Any


def generate_classes(data: list, attributes: list):
    data = data.copy()
    formatted_classes = []
    typing = [TypedDict, Optional, Literal, Union, Any]
    __globals = {
        item.__name__: item
        for item in typing
    }
    while len(data) > 0:
        cls = data.pop(0)
        formatted = format_class(cls)
        try:
            exec(formatted, __globals, __locals := {})
            __globals.update(__locals)
        except NameError as exc:
            if exc.name not in __globals:
                data.append(cls)
                continue
        formatted_classes.append(formatted)
    return "\n\n\n".join([
        "from typing import " + ", ".join([item.__name__ for item in typing]),
        *formatted_classes,
        *attributes
    ])


def format_class(cls: dict):
    if cls["bases"] != "TypedDict":
        raise NotImplementedError
    name = cls["name"].split(".")[-1]
    return f"class {name}(TypedDict):\n" + tab("\n".join([
        '"""',
        format_documentation(cls["description"], cls["attrs"]),
        '"""',
        '',
        format_attributes(name, cls["attrs"])
    ]))


def format_documentation(description: str, attributes: list[dict]) -> str:
    lines = []
    if len(description) > 0:
        lines.append(description)
        lines.append("")
    lines.append("Attributes:")
    lines.extend([
        f"    {attr["name"]}: {attr.get("type", "Any")} - {attr["description"]}"
        for attr in attributes
    ])
    return "\n".join(lines)


def format_attributes(cls_name: str, attributes: list[dict]) -> str:
    attrs = []
    for attr in attributes:
        type_ = attr.get("type", "Any")
        if cls_name in type_:
            type_ = '"' + type_ + '"'
        attrs.append(f"{attr["name"]}: {type_}")
    return "\n".join(attrs)


def generate_methods(data: list[dict]):
    return (
        "from .classes import *\n"
        "from .client import Client, api\n"
        "\n"
        "\n"
        "class Mathesar(Client):\n" +
        tab("\n\n".join(map(format_method, data)))
    )


def format_method(data: dict) -> str:
    name: str = data["name"]
    if "params" in data:
        params = parse_params(data["params"])
        if len(params) > 0:
            params = f", *, {params}"
    else:
        params = ""
    description = parse_description(data.get("description"), data.get("params", []), data.get("return"))
    if len(description) > 0:
        body = '"""\n' + description + '\n"""\n\n...'
    else:
        body = "..."
    if (return_ := data.get("return", {"type": "None"})["type"]) != "None":
        return_ = f" -> {return_}"
    else:
        return_ = ""
    out = (
        f"@api(\"{name}\")\n"
        f"def {name.replace(".", "_")}(self{params}){return_}:\n" + tab(body)
    )
    return out


def parse_description(description: str | None, params: list, return_: dict | None):
    result = ""
    if return_ is not None:
        ret_desc = return_.get("description", "")
    else:
        ret_desc = ""
    if description is not None and len(description) > 0:
        result += description
        if len(params) > 0 or len(ret_desc) > 0:
            result += "\n\n"
    lines = []
    if len(params) > 0:
        for param in params:
            lines.append(":param " + param["name"] + ": " + param["description"])
    if len(ret_desc) > 0:
        lines.append(":return: " + ret_desc)
    result += "\n".join(lines)
    return result


def parse_params(params: list):
    parsed = ", ".join(map(parse_param, params))
    return parsed


def parse_param(param: dict):
    type_ = param["type"]
    if type_ == "":
        type_ = "Any"
    out = param["name"] + ": " + type_
    if "default" in param:
        out += " = " + param["default"]
    return out


def tab(text: str, n: int = 1):
    return "\n".join([
        "    " * n + row
        for row in text.splitlines()
    ])


if __name__ == "__main__":
    cwd = Path(__file__).parent
    root = cwd / ".." / "src" / "commonspider_mathesarpy"
    with open(cwd / "scrape_results") as f:
        scrape_result = json.load(f)
    methods = generate_methods(scrape_result["methods"])
    with open(root / "api.py", "w") as f:
        f.write(methods)
    classes = generate_classes(scrape_result["classes"], scrape_result["attributes"])
    with open(root / "classes.py", "w") as f:
        f.write(classes)
