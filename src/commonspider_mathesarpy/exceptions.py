from collections import defaultdict


def raise_for_exception(data: dict):
    if error := data.get("error"):
        code = error.get("code")
        raise exceptions[code](error["message"])


class MathesarException(Exception):
    def __init_subclass__(cls, code: int, **kwargs):
        exceptions[code] = cls


exceptions = defaultdict(lambda: MathesarException)


class DoesNotExist(MathesarException, code=-28009):
    ...


class IntegrityError(MathesarException, code=-29042):
    ...


class DuplicateObject(MathesarException, code=-30047):
    ...


class SyntaxError(MathesarException, code=-30237):
    ...


class UndefinedObject(MathesarException, code=-30257):
    ...


class Unauthorized(MathesarException, code=-32603):
    ...
