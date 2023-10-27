def find_common_participants(first, second, splitter=','):
    participants = []  # Создадим "заготовку" под будущий список
    first_split = list(first.split(splitter))  # Разделим строку, преобразуем в список
    second_split = list(second.split(splitter))
    for person in first_split:  # Находим общих участников
        if person in second_split:  # Условие на "общность" участников
            participants.append(person)  # Добавляем в наш список
    participants.sort()  # Сортируем список
    return participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, '|'))
