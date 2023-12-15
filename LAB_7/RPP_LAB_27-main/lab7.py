import requests
import time

url = 'http://127.0.0.1:5000/v1/login'

#Мы изменяем данные в каждом задании для проверки
users_list = [
    {"email": "meow3@bk.ru", "password": "1234568"},
    {"email": "meow4@bk.ru", "password": "1234569"},
    {"email": "meow5@bk.ru", "password": "1234565"},
    {"email": "meow6@bk.ru", "password": "1234564"},
    {"email": "meow7@bk.ru", "password": "1234563"},
    {"email": "natasha@b.y1", "password": "123456"},
    {"email": "meow8@bk.ru", "password": "1234562"},
    {"email": "meow9@bk.ru", "password": "1234561"},
    {"email": "meow10@bk.ru", "password": "1234566"},
    {"email": "meow11@bk.ru", "password": "12345612"},
    {"email": "meow12@bk.ru", "password": "12345613"},
    {"email": "meow13@bk.ru", "password": "12345614"},
    {"email": "meow7@bk.ru", "password": "1234563"},
    {"email": "meow8@bk.ru", "password": "1234562"},
    {"email": "meow9@bk.ru", "password": "1234561"},
    {"email": "meow10@bk.ru", "password": "1234566"},
    {"email": "meow11@bk.ru", "password": "12345612"},
    {"email": "meow12@bk.ru", "password": "12345613"},
    {"email": "meow13@bk.ru", "password": "12345614"},
    {"email": "meow7@bk.ru", "password": "1234563"},
    {"email": "meow8@bk.ru", "password": "1234562"},
    {"email": "meow9@bk.ru", "password": "1234561"},
    {"email": "meow10@bk.ru", "password": "1234566"},
    {"email": "meow11@bk.ru", "password": "12345612"},
    {"email": "meow12@bk.ru", "password": "12345613"},
    {"email": "meow13@bk.ru", "password": "12345614"}
]

for user in users_list:
    payload = {
        'email': user['email'],
        'password': user['password']}
    response = requests.post(url, data=payload)

    if response.status_code == 429:
        print(f'Слишком много запросов. Пауза на 1 минуту...,  {response.status_code}')
        time.sleep(60)
    elif response.status_code == 200:
        print(f'Username: {user["email"]}, Password: {user["password"]}, {response.status_code}')
        break
    else:
        print(f'Неверно введены данные, {response.status_code}')
        continue

