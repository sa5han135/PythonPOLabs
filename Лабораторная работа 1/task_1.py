numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

numbers[4] = 0  # Заменяем элемент 'None' для правильной работы функций

sum_numbers = sum(numbers)  # Вычисление суммы списка
count_numbers = len(numbers)  # Вычисление количества элементов в списк
average_numbers = sum_numbers / count_numbers  # Нахождение среднего арифметического элементов списка

numbers[4] = average_numbers  # Замена пропущенного элемента

print("Измененный список:", numbers)
