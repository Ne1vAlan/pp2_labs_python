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