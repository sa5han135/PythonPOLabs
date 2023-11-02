import csv  # Подключим необходимые модули
import json

INPUT_FILENAME = "input.csv"  # Введем названия файлов как постоянные (для удобства)
OUTPUT_FILENAME = "output.json"


def task() -> None:
    data = []  # В список будем загружать десериализованные данные, полученные из csv-файла
    with open(INPUT_FILENAME, 'r') as file_csv:  # Открываем файл для чтения
        reader = csv.DictReader(file_csv)
        for row in reader:  # Читая данные в файле по строкам...
            data.append(row)  # ...добавляем их в список

    with open(OUTPUT_FILENAME, 'w') as file_json:  # Откроем файл для записи json-файла
        data_json = json.dumps(data, indent=4)  # Примем отступы, равным 4, и начнем сериализацию данных
        file_json.write(data_json)  # Запишем полученные данные в json-файл


if __name__ == '__main__':
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
