import inspect
import random
from functools import wraps
from typing import Any
from urllib.parse import urljoin

from bs4 import BeautifulSoup
from requests import Session


class Client:
    def __init__(self, url: str):
        self._url = url
        self._session = Session()

    def login(self, username: str, password: str):
        login_url = urljoin(self._url, "/auth/login/")

        response = self._session.get(login_url)
        dom = BeautifulSoup(response.text)
        token = dom.find("input", {"name": "csrfmiddlewaretoken"})["value"]

        response = self._session.post(
            login_url,
            data={
                "username": username,
                "password": password,
                "csrfmiddlewaretoken": token,
            },
            headers={
                "Referer": login_url
            }
        )
        content = response.text
        response.raise_for_status()

    def request(self, method: str, params: dict[str, Any]):
        response = self._session.post(
            urljoin(self._url, "/api/rpc/v0/"),
            headers={
                "X-CSRFToken": self._session.cookies["csrftoken"],
            },
            json={
                "jsonrpc": "2.0",
                "id": random.randint(1, 99999),
                "method": method,
                "params": params,
            }
        )
        data = response.json()
        if error := data.get("error"):
            raise Exception(error["message"])
        return data["result"]


methods_params = {}


def api(endpoint: str):
    def decorator(function):
        @wraps(function)
        def wrapper(self: Client, **kwargs):
            return self.request(endpoint, kwargs)

        methods_params[endpoint] = params = {
            param.name: param.annotation
            for param in inspect.signature(function).parameters.values()
        }
        params.pop("self", None)
        return wrapper
    return decorator
