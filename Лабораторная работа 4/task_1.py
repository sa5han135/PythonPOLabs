import doctest
from typing import Union


class Car:
    def __init__(self, max_speed: Union[int, float], durability: Union[int, float]):
        self.max_speed = max_speed
        self.durability = durability
        """
        Создание и подготовка к работе объекта "Машина"

        :param max_speed: Максимальная скорость машины
        :param durability: Прочность машины

        Примеры:
        >>> porsche = Car(250, 100)  # инициализация экземпляра класса
        """

    def is_car_running(self) -> bool:
        """
               Функция проверяет, заведена ли машина.
               :return: Заведена ли машина

               Примеры:
               >>> porsche = Car(250, 50)
               >>> porsche.is_car_running()
        """
        ...

    def car_repair(self, repair: Union[int, float]) -> None:
        """
               Ремонт машины, восстановление её прочности.
               :param repair: Запас прочности, восстанавливаемый машине

               :raise ValueError: Вызываем ошибку, если количество нитро превышает максимальное значение

               Примеры:
               >>> porsche = Car(250, 50)
               >>> porsche.car_repair(25)
        """
        if not isinstance(repair, (float, int)):
            raise TypeError("Запас прочности машины является числом")
        if repair < 0:
            raise ValueError("Запас прочности не может быть отрицательным")
        ...

    def car_nitro(self, nitro: Union[int, float]) -> None:
        """
               Нитро-ускорение машины.
               :param nitro: Остаток нитро-ускорения у машины

               :raise ValueError: Вызываем ошибку, если игрок пытается увеличить полностью заполненную шкалу нитро

               Примеры:
               >>> porsche = Car(250, 20)
               >>> porsche.car_nitro(75)
        """
        if not isinstance(nitro, (int, float)):
            raise TypeError("Остаток нитро-ускорения должно быть числом")
        if nitro < 0:
            raise ValueError("Остаток нитро-ускорения не может быть отрицательным")
        ...

    def __str__(self):
        return f"Максимальная скорость: {self.max_speed}. Запас прочности: {self.durability}"

    def __repr__(self):
        return f"{self.__class__.__name__}(max_speed={self.max_speed!r}, durability={self.durability!r}"


class PoliceCar(Car):
    def __init__(self, max_speed: Union[int, float], strength: Union[int, float], police_lights: bool):
        super().__init__(max_speed, strength)
        self.police_lights = police_lights
        """
        Создание и подготовка к работе объекта "Полицейская машина"

        :param police_lights: Определяет, включена ли полицейская сирена

        Примеры:
        >>> challenger = PoliceCar(250, 100, true)  # инициализация экземпляра класса
        """

    def police_spikes(self, spikes_damage: Union[int, float], spikes_amount: int) -> None:
        """
               Полицейские шипы для остановки гонщиков.
               :param spikes_damage: Урон от шипов, наносимый другим машинам
               :param spikes_amount: Остаток шипов у полицесйкой машины

               Примеры:
               >>> challenger = PoliceCar(250, 50, True)
               >>> challenger.police_spikes(20, 3)
               """
        if not isinstance(spikes_damage, (float, int)):
            raise TypeError("Урон от шипов должен быть числом")
        if spikes_damage < 0:
            raise ValueError("Шипы не могут наносить отрицательный урон")
        if not isinstance(spikes_amount, int):
            raise ValueError("Количество шипов должно быть целым числом")
        ...

    def car_nitro(self, nitro: Union[int, float]) -> None:
        super().car_nitro(nitro)
        """
               Нитро-ускорение машины.
               Перегрузка необходима, т.к. у полицейских нитро-ускорение тратится быстрее, восстанавливается медленнее
               
               param nitro: Остаток нитро-ускорения у машины

               :raise ValueError: Вызываем ошибку, если игрок пытается увеличить полностью заполненную шкалу нитро

               Примеры:
               >>> challenger = PoliceCar(250, 100, True)
               >>> challenger.car_nitro(50)
        """

    def __str__(self):
        return f"Машина готова к преследованию. {super().__str__()}. Включение сирены: {self.police_lights}"

    def __repr__(self):
        return f"{self.__class__.__name__}(max_speed={self.max_speed!r}, durability={self.durability!r}, police_lights={self.police_lights!r}"


class RacerCar(Car):
    def __init__(self, max_speed: Union[int, float], strength: Union[int, float], racer_radio: bool):
        super().__init__(max_speed, strength)
        self.racer_radio = racer_radio
        """
        Создание и подготовка к работе объекта "Гоночная машина"

        :param racer_radio: Наличие 'прослушки' полицейской частоты

        Примеры:
        >>> bmw = RacerCar(250, 100, False)  # инициализация экземпляра класса
        """

    def racer_jammer(self, jammer_time: Union[int, float], jammer_amount: int) -> None:
        """
               Гоночная 'глушилка', для подавления оружия полицесйких
               :param jammer_time: Время действия "глушилки"
               :param jammer_amount: Оставшееся количество "глушилок"

               Примеры:
               >>> bmw = RacerCar(250, 50, False)
               >>> bmw.racer_jammer(15, 2)
        """
        if not isinstance(jammer_time, (float, int)):
            raise TypeError("Время действия 'глушилки' должно быть числом")
        if jammer_time < 0:
            raise ValueError("Время действия 'глушилки' не может быть отрицательно")
        if not isinstance(jammer_amount, int):
            raise ValueError("Количество 'глушилок' должно должно быть целым числом")
        ...

    def car_repair(self, nitro: Union[int, float]) -> None:
        super().car_repair(nitro)
        """
               Ремонт машины, восстановление её прочности.
               Перегрузка необходима, т.к. у гонщиков прочность тратится быстрее, восстанавливается медленнее
               
               :param repair: Запас прочности, восстанавливаемый машине

               :raise ValueError: Вызываем ошибку, если количество нитро превышает максимальное значение

               Примеры:
               >>> bmw = Car(250, 50)
               >>> bmw.car_repair(25)
        """

    def __str__(self):
        return f"Машина готова к гонке. {super().__str__()}. Наличие 'прослушки': {self.racer_radio}"

    def __repr__(self):
        return f"{self.__class__.__name__}(max_speed={self.max_speed!r}, durability={self.durability!r}, police_lights={self.racer_radio!r}"


if __name__ == "__main__":
    doctest.testmod()
    pass
