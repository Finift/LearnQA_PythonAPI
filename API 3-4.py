#User Agent - это один из заголовков, позволяющий серверу узнавать, с какого девайса и браузера пришел запрос. Он формируется автоматически клиентом, например браузером. Определив, с какого девайса или браузера пришел к нам пользователь мы сможем отдать ему только тот контент, который ему нужен.
#Наш разработчик написал метод: https://playground.learnqa.ru/ajax/api/user_agent_check
#Метод определяет по строке заголовка User Agent следующие параметры:
#device - iOS или Android
# browser - Chrome, Firefox или другой браузер
# platform - мобильное приложение или веб
# Если метод не может определить какой-то из параметров, он выставляет значение Unknown.
# Наша задача написать параметризированный тест. Этот тест должен брать из дата-провайдера User Agent и ожидаемые значения, GET-делать запрос с этим User Agent и убеждаться, что результат работы нашего метода правильный - т.е. в ответе ожидаемое значение всех трех полей.


import requests
import pytest_check as check


dictionary = {
    'Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30': {'platform': 'Mobile', 'browser': 'No', 'device': 'Android'},
    'Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1': {'platform': 'Mobile', 'browser': 'No', 'device': 'iOS'},
    'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)': {'platform': 'Unknown', 'browser': 'Unknown', 'device': 'Unknown'},
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0': {'platform': 'Web', 'browser': 'Chrome', 'device': 'No'},
    'Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1': {'platform': 'Mobile', 'browser': 'No', 'device': 'Unknown'}
}


class TestAgent:
    def test_user_agents(self):
        for key, value in dictionary.items():
            response = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check", headers={"User-Agent": key})
            check.equal(response.json()['platform'], value['platform']), 'Platform wrong'
            check.equal(response.json()['browser'], value['browser']), 'browser wrong'
            check.equal(response.json()['device'], value['device']), 'device wrong'
            print(response.text, response.json()['platform'], response.json()['browser'], response.json()['device'])


