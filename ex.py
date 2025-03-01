import json

# Открываем JSON-файл и загружаем данные
with open(r"D:\gitHub\pp2_labs_python\text.json", "r", encoding="utf-8") as file:
    data = json.load(file)  # Загружаем JSON в переменную data

# Проверяем, есть ли ключ "_embedded" -> "episodes"
    # Перебираем все эпизоды
    for episode in data["_embedded"]["episodes"]:
        name = episode.get("name", "")  # Название эпизода
        season = episode.get("season", "")  # Номер сезона
        number = episode.get("number", "")  # Номер эпизода
        rating = episode.get("rating", {}).get("average", 0)  # Достаем рейтинг (по умолчанию 0)

        # Проверяем, больше ли рейтинг 4.5
        if rating > 4.5:
            print(f"Сезон {season}, Эпизод {number}: {name} (Рейтинг: {rating})")
