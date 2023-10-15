list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

average_len = int(len(list_players) / 2)  # Создадим переменную, равную половине длины строки
first_team = list_players[0:average_len]  # Найдем первую команду
print(first_team)
second_team = list_players[average_len:len(list_players)]  # Найдем вторую команду
print(second_team)
