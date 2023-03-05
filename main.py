import requests
from json.decoder import JSONDecodeError

# payload = {"name": "Petrov"}
# response = requests.get("https://playground.learnqa.ru/api/hello",
#                         params=payload)
# print(response.text)

response = requests.get("https://playground.learnqa.ru/api/get_text")
print(response.text)

try:
    parsed_response_text = response.json()
    print(parsed_response_text)
except JSONDecodeError:
    print("response is not JSON format")



