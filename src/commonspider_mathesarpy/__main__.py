import json
import typing
from argparse import ArgumentParser

from typing import TypedDict

from .client import methods_params
from .api import Mathesar

argparse = ArgumentParser(prog="mathesarpy")
argparse.add_argument("--url", required=True)
argparse.add_argument("--username", required=True)
argparse.add_argument("--password", required=True)
argparse.add_argument("method")
argparse.add_argument("args", nargs="*")

def run_argv(*argv):
    if len(argv) == 0:
        argv = None
    args = argparse.parse_args(argv)

    client = Mathesar(args.url)
    client.login(args.username, args.password)
    method = args.method
    args = parse_args(methods_params[method], args.args)

    return getattr(client, method.replace(".", "_"))(**args)


def parse_args(params: dict, args):
    out = {}
    for (name, ann), val in zip(params.items(), args):
        if isinstance(ann, typing._TypedDictMeta):
            out[name] = json.loads(val)
        else:
            raise NotImplementedError
    return out

if __name__ == "__main__":
    run_argv()
