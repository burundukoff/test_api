import json

json_string = '{"answer": "Hello, User"}'
obj = json.loads(json_string)
key = "answer"

if key in obj:
    print(obj[key])
else:
    print(f"ключ {key} в JSON не найден")    
