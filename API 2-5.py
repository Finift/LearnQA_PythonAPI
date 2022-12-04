import requests
from bs4 import BeautifulSoup

URL = "https://playground.learnqa.ru/ajax/api/get_secret_password_homework"
URL2 = "https://playground.learnqa.ru/ajax/api/check_auth_cookie"
URL3 = "https://en.wikipedia.org/wiki/List_of_the_most_common_passwords"

passwords = requests.get(URL3)
soup = BeautifulSoup(passwords.text, 'lxml')
print(soup)
# response = requests.get(URL, params={'login': "super_admin"})
# print(response.cookies)
#
# auth_check = requests.get(URL2, params={'cookie': response.cookies})
# print(auth_check.text)
