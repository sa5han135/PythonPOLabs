# TODO Напишите функцию для поиска индекса товара
def item_search(item_list, item_found):
    for i in range(len(item_list)):  # С помощью цикла пройдемся по списку
        if item_list[i] == item_found:  # Условие на нахождение нужного предмета
            return i
    return None


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = item_search(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
