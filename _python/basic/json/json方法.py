import json

dictionary = {
    'zn': 'zn'
}
json_dumps = json.dumps(dictionary)
print(json_dumps)
json_loads = json.loads(json_dumps)
print(json_loads)
# json.load格式必须为外面单引号，里面双引号
# json_loads = json.loads('{"zn": "zn"}')
json_loads = json.loads("{'zn': 'zn'}")
print(json_loads)
