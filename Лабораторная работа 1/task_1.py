import doctest
from typing import Union


class Weapon:
    def __init__(self, bullets: int, damage: int):
        """
        Создание и подготовка к работе объекта "Оружие"

        :param bullets: Количество патронов в магазине оружия
        :param damage: Наносимый оружием урон противнику

        Примеры:
        >>> ak47 = Weapon(30, 35)  # инициализация экземпляра класса
        """
        if not isinstance(bullets, int):
            raise TypeError("Количество патронов должно быть целым числом")
        if bullets < 0:
            raise ValueError("Количество патронов не может быть отрицательно")
        self.bullets = bullets

        if not isinstance(damage, (int, float)):
            raise TypeError("Урон должен быть числом")
        if damage < 0:
            raise ValueError("Урон от оружия не может быть отрицательным")
        self.damage = damage

    def weapon_reload(self, inv_bullets: int) -> None:
        """
               Перезарядка оружия.
               :param inv_bullets: Добавление патронов, находящихся в инвентаре игрока в магазин оружия

               :raise ValueError: Вызываем ошибку, если в инвентаре игрока отсутствуют патроны

               Примеры:
               >>> ak47 = Weapon(15, 35)
               >>> ak47.weapon_reload(15)
               """
        if not isinstance(inv_bullets, int):
            raise TypeError("Количество добавляемых патронов должно быть целым числом")
        if inv_bullets < 0:
            raise ValueError("Количество добавляемых патронов не должно быть отрицательным")
        ...

    def is_weapon_broke(self) -> bool:
        """
               Функция проверки поломки оружия.
               :return: Является ли оружие сломанным

               Примеры:
               >>> ak47 = Weapon(30, 35)
               >>> ak47.is_weapon_broke()
               """
        ...

    def weapon_add_damage(self, damage_bonus: int) -> None:
        """
               Повышение урона оружия.
               :param damage_bonus: Значение бонуса, увеличивающего урон оружия

               :raise ValueError: Вызываем ошибку, если бонус превышает максимальный урон в игре

               Примеры:
               >>> ak47 = Weapon(30, 35)
               >>> ak47.weapon_add_damage(15)
               """
        if not isinstance(damage_bonus, (float, int)):
            raise TypeError("Бонус к урону должен быть числом")
        if damage_bonus <= 0:
            raise ValueError("Бонус к урону должен быть положительным числом")
        ...


class Car:
    def __init__(self, speed: Union[int, float], fuel: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Машина"

        :param speed: Скорость передвижения машины
        :param fuel: Оставшееся топливо в баке

        Примеры:
        >>> banshee = Car(250, 50)  # инициализация экземпляра класса
        """
        if not isinstance(speed, (int, float)):
            raise TypeError("Скорость машины должна быть числом")
        if speed < 0:
            raise ValueError("Скорость машины должна быть положительным числом")
        self.speed = speed

        if not isinstance(fuel, (int, float)):
            raise TypeError("Количество топлива должно быть числом")
        if fuel < 0:
            raise ValueError("Количество топлива не может быть отрицательным числом")
        self.fuel = fuel

    def car_fuelling(self, station_fuel: Union[int, float]) -> None:
        """
               Перезарядка оружия.
               :param station_fuel: Количество топлива на заправке

               :raise ValueError: Вызываем ошибку, если игрок пытается заправить полностью заправленную машину

               Примеры:
               >>> banshee = Car(250, 20)
               >>> banshee.car_fuelling(30)
               """
        if not isinstance(station_fuel, (int, float)):
            raise TypeError("Количество топлива на заправке должно быть числом")
        if station_fuel < 0:
            raise ValueError("Количество топлива на заправке не может быть отрицательно")
        ...

    def is_car_running(self) -> bool:
        """
               Функция которая проверяет заведена ли машина.
               :return: Заведена ли машина

               Примеры:
               >>> banshee = Car(250, 50)
               >>> banshee.is_car_running()
               """
        ...

    def car_nitro(self, nitro: Union[int, float]) -> None:
        """
               Повышение урона оружия.
               :param nitro: Количество нитро у машины

               :raise ValueError: Вызываем ошибку, если количество нитро превышает максимальное значение

               Примеры:
               >>> banshee = Car(250, 50)
               >>> banshee.car_nitro(25)
               """
        if not isinstance(nitro, (float, int)):
            raise TypeError("Количество нитро должно быть числом")
        if nitro < 0:
            raise ValueError("Количество нитро не может быть меньше нуля")
        ...


class Guitar:
    def __init__(self, strings: int, volume: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Гитара"

        :param strings: Количество струн на гитаре
        :param volume: Громкость гитары

        Примеры:
        >>> mustang = Guitar(6, 75)  # инициализация экземпляра класса
        """
        if not isinstance(strings, int):
            raise TypeError("Количество струн должно быть целым числом")
        if strings <= 0:
            raise ValueError("Количество струн должно быть положительным числом")
        self.strings = strings

        if not isinstance(volume, (int, float)):
            raise TypeError("Громкость гитары должна быть числом")
        if volume < 0:
            raise ValueError("Громкость гитары не может быть отрицательным числом")
        self.volume = volume

    def guitar_distortion(self, distortion_level: Union[int, float], distortion_gain: Union[int, float]) -> None:
        """
               Уровень перегруза гитары.
               :param distortion_level: Уровень громкости перегруза гитары

               :param distortion_gain: Мощность перегруза гитары

               Примеры:
               >>> mustang = Guitar(6, 75)
               >>> mustang.guitar_distortion(90, 85)
               """
        if not isinstance(distortion_level, (int, float)):
            raise TypeError("Громкость перегруза гитары должна быть числом")
        if distortion_level < 0:
            raise ValueError("Громкость перегруза не может быть отрицательна")

        if not isinstance(distortion_gain, (int, float)):
            raise TypeError("Мощность перегруза гитары должна быть числом")
        if distortion_gain < 0:
            raise ValueError("Мощность перегруза не может быть отрицательна")
        ...

    def is_guitar_connect(self) -> bool:
        """
               Функция которая проверяет подключена ли гитара к усилителю.
               :return: Подключена ли гитара к усилителю

               Примеры:
               >>> mustang = Guitar(6, 75)
               >>> mustang.is_guitar_connect()
               """
        ...

    def guitar_reverb(self, reverb_volume: Union[int, float], reverb_time: Union[int, float]) -> None:
        """
               Уровень эффекта реверберации гитары.
               :param reverb_volume: Уровень эффекта реверберации

               :param reverb_time: Продолжительность эффекта реверберации

               Примеры:
               >>> mustang = Guitar(6, 75)
               >>> mustang.guitar_reverb(50, 0.5)
               """
        if not isinstance(reverb_volume, (float, int)):
            raise TypeError("Уровень эффекта должен быть числом")
        if reverb_volume < 0:
            raise ValueError("Уровень эффекта не может быть меньше нуля")

        if not isinstance(reverb_time, (int, float)):
            raise TypeError("Длительность эффекта должна быть числом")
        if reverb_time < 0:
            raise ValueError("Длительность эффекта не может быть отрицательным числом")
        ...


if __name__ == "__main__":
    doctest.testmod()  # Проводим проверку примеров, приведенных в документации
