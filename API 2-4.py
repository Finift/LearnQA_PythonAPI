# Наша задача - написать скрипт, который делал бы следующее:
# 1) создавал задачу
# 2) делал один запрос с token ДО того, как задача готова, убеждался в правильности поля status
# 3) ждал нужное количество секунд с помощью функции time.sleep() - для этого надо сделать import time
# 4) делал бы один запрос c token ПОСЛЕ того, как задача готова, убеждался в правильности поля status и наличии поля result
import requests
import time


URL = "https://playground.learnqa.ru/ajax/api/longtime_job"

response = requests.get(URL)
if "result" not in response:
    response1 = requests.get(URL, params={'token': response.json()['token']})
    print(response1.text)
    if response1.json()['status'] == "Job is NOT ready":
        print(f"Wait {response.json()['seconds']} sec")
        time.sleep(response.json()['seconds'])
        response = requests.get(URL, params={'token': response.json()['token']})
        if response.json()['status'] == "Job is ready" and response.json()["result"] != "":
            print(response.text)
