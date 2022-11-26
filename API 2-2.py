import requests
import json


response = requests.get("https://playground.learnqa.ru/api/long_redirect")
redirect_count = len(list(response.history))

response1 = response.history[0]
response2 = response.history[1]

print(response.url, response1, response2, redirect_count)
