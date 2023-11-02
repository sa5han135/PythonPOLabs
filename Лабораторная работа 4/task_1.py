import json

INPUT_FILE = "input.json"


def task() -> float:
    with open(INPUT_FILE, 'r') as file:  # Откроем JSON-файл
        data = json.load(file)
        result_list = []  # Создадим список для последующей работы
        for dicts in data:  # Из словарей JSON будем "доставать" данные...
            result_list.append(dicts['score'] * dicts['weight'])  # ...и добавлять в список их произведение
        result = sum(result_list)  # Суммируем все полученные произведения
        return round(result, 3)  # Вернем результат, округленный до 3 знаков


print(task())
