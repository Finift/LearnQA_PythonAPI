# Необходимо написать скрипт, который создает GET-запрос на метод: https://playground.learnqa.ru/api/long_redirect
# С помощью конструкции response.history необходимо узнать, сколько редиректов происходит от изначальной точки назначения до итоговой. И какой URL итоговый.
import requests
import json


response = requests.get("https://playground.learnqa.ru/api/long_redirect")
redirect_count = len(list(response.history))

response1 = response.history[0]
response2 = response.history[1]

print(response.url, response1, response2, redirect_count)
