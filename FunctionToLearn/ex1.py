import json

with open(r"D:\gitHub\pp2_labs_python\text.json", "r", encoding="utf-8") as file:
    data = json.load(file)

for laureate in data["laureates"]:
    name = laureate.get("firstname", "")
    surname = laureate.get("surname", "")

    print(f"{name} {surname}".strip())