import requests
import json


response = requests.get("https://playground.learnqa.ru/api/long_redirect")
response1 = response.history[0]
response2 = response.history[1]

redirect_count = len(list(response.history))
print(response.url, response1, response2, redirect_count)
