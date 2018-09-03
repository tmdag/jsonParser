Python 3 JsonParser
==============
![VFX Pipeline](https://img.shields.io/badge/VFX%20Pipeline-2018-lightgrey.svg?style=flat)
![python v3.6](https://img.shields.io/badge/Python-3.6-blue.svg?style=flat)
![pylint Score](https://mperlet.github.io/pybadge/badges/8.80.svg)

GitHub: https://github.com/tmdag/jsonParser

## Overview
A wrapper on top of original python `json` module.

## Usage:
```
from jsonParser import JsonFile
my_json = JsonFile("some/json_file.json").load()
print(my_json)

data = {}
data['info'] = {}
data['info']['year'] = 2018

JsonFile("some/json_file.json").save(data)
```

