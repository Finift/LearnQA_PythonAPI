#Необходимо написать тест, который делает запрос на метод: https://playground.learnqa.ru/api/homework_header
#Этот метод возвращает headers с каким-то значением. Необходимо с помощью функции print() понять что за headers и с каким значением, и зафиксировать это поведение с помощью assert
import requests
import datetime


dt_obj = datetime.datetime.now()
dt_obj -= datetime.timedelta(hours=3)
dt_string = dt_obj.strftime("%a, %d %b %Y %H:%M:%S GMT")


class Test3:
    def test_header(self):
        url = 'https://playground.learnqa.ru/api/homework_header'
        payload = {'Date': dt_string, 'Content-Type': 'application/json', 'Content-Length': '15', 'Connection': 'keep-alive', 'Keep-Alive': 'timeout=10', 'Server': 'Apache', 'x-secret-homework-header': 'Some secret value', 'Cache-Control': 'max-age=0', 'Expires': dt_string}
        response = requests.get(url, params=payload)
        response_header = response.headers
        assert dict(response_header) == payload, 'Wrong request'
