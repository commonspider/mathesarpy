# Mathesarpy
Unofficial python bindings for the Mathesar API.

## Installation
```
pip install -i https://test.pypi.org/simple/ commonspider-mathesarpy
```

## Usage
```
from commonspider_mathesarpy import Mathesar

mathesar = Mathesar("https://your.mathesar.url")
mathesar.login("username", "password")

# Now you can do API calls. E.g.:
mathesar.users_list()
```

## Documentation
All methods are self documented and they work with Mathesar 0.4.0.

For more information read the official [documentation](https://docs.mathesar.org/0.4.0/api/methods/).
