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
