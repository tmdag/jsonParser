# Python 3 JsonParser
A wrapper on top of original python `json` module.

## Example:
```
from jsonParser import JsonFile
my_json = JsonFile("some/json_file.json").load()
print(my_json)

data = {}
data['info'] = {}
data['info']['year'] = 2018

JsonFile("some/json_file.json").save(data)
```

