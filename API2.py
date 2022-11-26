# Давайте создадим пустой Python-скрипт.
# Внутри него создадим переменную json_text. Значение этой переменной должно быть таким, как указано тут: https://gist.github.com/KotovVitaliy/83e4eeabdd556431374dfc70d0ba9d37
# Наша задача с помощью библиотеки “json”, которую мы показывали на занятии, распарсить нашу переменную json_text и вывести текст второго сообщения с помощью функции print.

import requests
import json

json_text = "https://gist.github.com/KotovVitaliy/83e4eeabdd556431374dfc70d0ba9d37"
response = requests.get(json_text)
result = list(response)
print(result[1])
