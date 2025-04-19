import json
# json转字符串
data = [{'name': 'zs', 'age': 11},{'name': 'ls', 'age': 12},{'name': 'ww', 'age': 13}]

json_str = json.dumps(data, ensure_ascii=False)

print(json_str)

d = {'zs': 12, 'ls': 13}
json_str = json.dumps(d, ensure_ascii=False)
print(json_str)


# 字符串转json
s = '[{"name": "zs", "age": 11}, {"name": "ls", "age": 12}, {"name": "ww", "age": 13}]'
l = json.loads(s)
print(l)
print(type(l))

s = '{"zs": 12, "ls": 13}'
l = json.loads(s)
print(l)
print(type(l))