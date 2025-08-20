import json
from collections.abc import Iterable
from pathlib import Path
from typing import Any

import requests
from bs4 import BeautifulSoup, Tag, PageElement

replace_attr_type = {
    "ConfiguredServerInfo": "Any"
}

replace_return_type = {
    "ConstraintInfo": "Any"
}


def scrape():
    dom = BeautifulSoup(
        requests.get("https://docs.mathesar.org/0.4.0/api/methods/").text,
        features="html.parser"
    )
    return {
        "methods": list(map(scrape_function, dom.find_all("div", {"class": "doc-function"}))),
        "classes": list(map(scrape_class, dom.find_all("div", {"class": "doc-class"}))),
        "attributes": list(map(scrape_attribute, dom.find_all("div", {"class": "doc-attribute"})))
    }


def scrape_function(doc_function: Tag):
    name = doc_function.find("h3", {"class": "doc-heading"}).text.replace("¶", "").strip()
    if name.endswith("_"):
        name = name[:-1]
    out: dict[str, Any] = {"name": name}
    content = [
        item
        for item in doc_function.find("div", {"class": "doc-contents"}).children
        if item != "\n"
    ]
    reversed_content = reversed(content)
    for item in reversed_content:
        if not isinstance(item, Tag):
            raise ValueError
        if item.name == "details":
            continue
        elif item.name == "table":
            title = next(reversed_content).text.strip()
            if title == "Returns:":
                out["return"] = scrape_return(item)
            elif title == "Parameters:":
                out["params"] = scrape_parameters(item)
            elif title == "Attributes:":
                out["params"] = scrape_attributes(item)
            else:
                raise ValueError
        elif item.name == "p":
            out["description"] = scrape_description(reversed([item.text, *reversed_content]))
            break
        else:
            raise ValueError
    return out


def scrape_return(table: Tag):
    rows = list(table.tbody.find_all("tr"))
    type_td, desc_td = rows[0].find_all("td")
    type_ = type_td.text.strip()
    for key, val in replace_return_type.items():
        type_ = type_.replace(key, val)
    desc = desc_td.text.strip()
    for row in rows[1:]:
        type_td, desc_td = row.find_all("td")
        if type_td.text.strip() != type_:
            raise ValueError
        desc += desc_td.text.strip()
    return {
        "type": type_,
        "description": desc
    }


def scrape_parameters(table: Tag):
    params = []
    for param_row in table.tbody.find_all("tr"):
        name_td, type_td, description_td, default_td = param_row.find_all("td")
        param = {
            "name": name_td.text.strip(),
            "type": type_td.text.strip(),
            "description": description_td.text.strip(),
        }
        default = default_td.text.strip()
        if default != "required":
            param["default"] = default
        params.append(param)
    return params


def scrape_class(doc_class: Tag):
    name = doc_class.find("h3", {"class": "doc-heading"}).text.replace("¶", "").strip()
    content = list(doc_class.find("div", {"class": "doc-contents"}).children)
    bases_p = content[1]
    if not isinstance(bases_p, Tag):
        raise ValueError
    if "doc-class-bases" not in bases_p["class"]:
        raise ValueError
    bases = bases_p.code.text.strip()
    end_index = len(content) - 2
    while end_index >= 0:
        tag = content[end_index]
        if not isinstance(tag, Tag) or tag.name != "table":
            end_index -= 2
            continue
        attrs = scrape_attributes(tag)
        break
    else:
        end_index = len(content) - 4
        tag = content[end_index]
        if not isinstance(tag, Tag):
            raise ValueError
        attrs = scrape_attributes_fallback(tag)
    description = scrape_description(content[3:end_index - 2])
    return {
        "name": name,
        "bases": bases,
        "attrs": attrs,
        "description": description
    }


def scrape_attributes(table: Tag):
    attrs = []
    for attr_row in table.tbody.find_all("tr"):
        name_td, type_td, description_td = attr_row.find_all("td")
        type_ = type_td.text.strip()
        for key, val in replace_attr_type.items():
            if type_ == key:
                type_ = val
                break
        attr = {
            "name": name_td.text.strip(),
            "type": type_,
            "description": description_td.text.strip(),
        }
        attrs.append(attr)
    return attrs


def scrape_attributes_fallback(tag: Tag):
    lines = iter(tag.text.splitlines())
    while next(lines) != "Attributes:":
        continue
    attrs = []
    for line in lines:
        name, description = line.split(":", maxsplit=1)
        attrs.append({
            "name": name.strip(),
            "description": description.strip()
        })
    return attrs


def scrape_description(elements: Iterable[PageElement]):
    return "\n".join([
        item.text if isinstance(item, Tag) else item
        for item in elements
    ]).strip()


def scrape_attribute(attribute: Tag):
    return attribute.find_all("code")[1].text.strip()


if __name__ == "__main__":
    path = Path(__file__).parent / "scrape_results"
    scrape_result = scrape()
    data = json.dumps(scrape_result, indent=2)
    with open(path, "w") as f:
        f.write(data)
