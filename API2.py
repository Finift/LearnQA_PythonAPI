import requests
import json

json_text = "https://gist.github.com/KotovVitaliy/83e4eeabdd556431374dfc70d0ba9d37"
response = requests.get(json_text)
result = list(response)
print(result[1])
