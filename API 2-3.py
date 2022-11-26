# Сегодня задача должна быть попроще. У нас есть вот такой URL: https://playground.learnqa.ru/ajax/api/compare_query_type
# Запрашивать его можно четырьмя разными HTTP-методами: POST, GET, PUT, DELETE
# При этом в запросе должен быть параметр method. Он должен содержать указание метода, с помощью которого вы делаете запрос. Например, если вы делаете GET-запрос, параметр method должен равняться строке ‘GET’. Если POST-запросом - то параметр method должен равняться ‘POST’.  И так далее.
# Надо написать скрипт, который делает следующее:
# 1. Делает http-запрос любого типа без параметра method, описать что будет выводиться в этом случае.
# 2. Делает http-запрос не из списка. Например, HEAD. Описать что будет выводиться в этом случае.
# 3. Делает запрос с правильным значением method. Описать что будет выводиться в этом случае.
# 4. С помощью цикла проверяет все возможные сочетания реальных типов запроса и значений параметра method. Например с GET-запросом передает значения параметра method равное ‘GET’, затем ‘POST’, ‘PUT’, ‘DELETE’ и так далее. И так для всех типов запроса. Найти такое сочетание, когда реальный тип запроса не совпадает со значением параметра, но сервер отвечает так, словно все ок. Или же наоборот, когда типы совпадают, но сервер считает, что это не так.
# Не забывайте, что для GET-запроса данные надо передавать через params=
# А для всех остальных через data=
import requests


URL = "https://playground.learnqa.ru/ajax/api/compare_query_type"

#Вопрос 1
content = requests.get(URL)
print(content, content.text, content.request)

#Вопрос 2
content2 = requests.head(URL)
print(content2, content2.request)

#Вопрос 3
list = ['get', 'post', 'put', 'delete']
content3 = requests.post(URL, data=list[1])
print(content3, content3.text, content3.request, f"method = {list[1]}")

#Вопрос 4
list2 = ['get', 'post', 'put', 'delete', 'head']
for i in range(0, len(list)):
    method = list[i]
    response = requests.get(URL, params=method)
    print(response, response.text, response.request, f"method = {method}")
    response1 = requests.post(URL, data=method)
    print(response1, response1.text, response1.request, f"method = {method}")
    response2 = requests.put(URL, data=method)
    print(response2, response2.text, response2.request, f"method = {method}")
    response3 = requests.delete(URL, data=method)
    print(response3, response3.text, response3.request, f"method = {method}")
    response4 = requests.head(URL, data=method)
    print(response4, response4.text, response4.request, f"method = {method}")
