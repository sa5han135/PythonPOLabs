money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

months = 0
remaind_money = money_capital  # Установим значение оставшихся денег

while remaind_money > spend:
    remaind_money += salary  # Получаем зарплату
    remaind_money -= spend  # Тратим её
    months += 1  # Считаем этот месяц прожитым без долгов
    if months == 1:  # Учитываем, что в первый месяц повышения цен нет
        continue
    spend *= 1 + increase  # Месячные расходы увеличиваются
print("Количество месяцев, которое можно протянуть без долгов:", months)
