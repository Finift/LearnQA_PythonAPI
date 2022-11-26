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
