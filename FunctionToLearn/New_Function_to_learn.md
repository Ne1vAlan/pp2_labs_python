numbers = list(map(int, input().split())) ->для введения листа(цифр) пользователем,

int - цифры или просто значения,

list - обозначения что мы делаем в листе,

input - для ввода пользователем,

split - разделяя наши значения или строки по пробелам,

map - обработка каждого элемента в итерируемом объекте, 

float - ввод с плавающей точкой,

pass - пропуск кода который не будет выдовать ошибку,

str - перевод в текст (стринг)

import - это как библиотека,

import math - библиотека математических значений,

import random - добовляет рандомные значения



"random.randint(1, 20)" - выдаст рандомное значения от 1 до 20


with open(r"D:\gitHub\pp2_labs_python\text.json", "r", encoding="utf-8") as file:
    data = json.load(file)  -- чтобы открыть файл через сам вс код

    for episode in data["_embedded"]["episodes"]:
        name = episode.get("name", "")
        season = episode.get("season", "")  
        number = episode.get("number", "")  -- выбрать имнно то что нужно, по названию 

        from datetime import datetime

date1 = datetime.strptime(date1_str, "%Y-%m-%d")
date2 = datetime.strptime(date2_str, "%Y-%m-%d") -- переводит строку в в дни




for prize in laureate.get("prizes", []):
            if prize.get("category") == "phy": 
                printf"{name} {surname}"


















def odd_numbers():
    num = 1
    while True:
        yield num ** 2 
        num += 2  

gen = odd_numbers()

for _ in range(10):
    print(next(gen))
