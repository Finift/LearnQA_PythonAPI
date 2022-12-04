#Необходимо написать тест, который делает запрос на метод: https://playground.learnqa.ru/api/homework_cookie
#Этот метод возвращает какую-то cookie с каким-то значением. Необходимо с помощью функции print() понять что за cookie и с каким значением, и зафиксировать это поведение с помощью assert
import requests


class Test2:
    def test_cookie(self):
        url = 'https://playground.learnqa.ru/api/homework_cookie'
        payload = {'HomeWork': 'hw_value'}
        response = requests.get(url, params=payload)
        response_cookie = response.cookies
        assert dict(response_cookie) == payload, 'Wrong request'
