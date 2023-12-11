class FlashDrive:
    """
    Документация на класс
    Класс описывает объем памяти флешки
    """
    def __init__(self, memory: float, occupied_memory: float):
        """
        Инициализация экземляра класса
        :param memory: Объем памяти флешки
        :param occupied_memory: Колличество занятой памяти
        """
        if not isinstance(memory, (int, float)):
            raise TypeError('Объем памяти должен быть типа int или float')
        if not memory > 0:
            raise ValueError('Объем памяти должен быть положительным числом')
        self.memory = memory

        if not isinstance(occupied_memory, (int, float)):
            raise TypeError('Объем занимаемой памяти должен быть типа int или float')
        if not occupied_memory > 0:
            raise ValueError('Объем занимаемой памяти должен быть положительным числом')
        self.occupied_memory = occupied_memory

    def is_empty_fd(self) -> bool:
        """
        Метод вычисляет пустая ли флешка

        Пример:
        >>> flash_drive = FlashDrive(1000, 0)
        >>> flash_drive.is_empty_fd()
        """
    ...

    def increace_the_occupied_memory(self, fail: float) -> None:
        """
        Метод добавления файлов на флешку
        :param fail: Вес добавленного файла

        Пример:
        >>> flash_drive = FlashDrive(1000, 0)
        >>> flash_drive.increace_the_occupied_memory(500)
        """

        if not isinstance(fail, (int, float)):
            raise TypeError('Объем файла должен быть типа int или float')
        if not fail > 0:
            raise ValueError('Объем файла должен быть положительным числом')
    ...


class FruitBox:
    """
        Документация на класс
        Класс описывает количество фруктов в коробке
        """
    def __init__(self, fruits: str, weight: int):
        """
        Инициализация экземляра класса
        :param fruits: Фрукты в коробке
        :param weight: Вес коробки
        """
        self.fruits = fruits
        self.weight = weight

    def new_weight(self, weight_new_fruits: int) -> None:
        """
        Метод увеличивает вес коробки.

        :weight_new_fruits: вес новых фруктов
        """
        if not isinstance(weight_new_fruits, int):  # проверяем, что вес новых фруктов типа int
            raise TypeError("Вес новых фруктов должен быть типа int")  # вызываем ошибку

        if weight_new_fruits < 0:
            raise ValueError("Вес новых фруктов должен быть положительным числом")

        self.new_weight += weight_new_fruits

    def remove_fruits_from_box(self, estimate_fruits: float) -> None:
        """
        Извлечение фруктов из коробки.

        :param estimate_fruits: Вес извлекаемых фруктов
        :raise ValueError: Если вес извлекаемых фруктов превышает вес коробки,
        то возвращается ошибка.

        :return: Вес реально извлеченных фруктов

        Примеры:
        >>> weight = FruitBox('Апельсины', 30)
        >>> weight.remove_fruits_from_box(10)
        """
    ...


class AtmosphericPrecipiation:
    """
        Документация на класс
        Класс описывает количество выпавших осадков
        """
    def __init__(self, precipiation: str, mm: int):
        """
        Инициализация экземляра класса
        :param precipiation: вид атмосферных осадков
        :param mm: колличество выпавших осадков в миллиметрах
        """
        self.precipiation = precipiation
        self.mm = mm

    def weather_forecast(self, forecast: float) -> None:
        """
        Прогноз колличества осадков.

        :param forecast: колличество загаданных осадков

        :return: Угадали или нет

        Примеры:
        >>> mm = AtmosphericPrecipiation('Дождь', 3)
        >>> mm.weather_forecast(3)
        """
    ...

    def rain_today(self) -> bool:
        """
        Метод вычисляет был ли сегодня дождь

        Пример:
        >>> weather= AtmosphericPrecipiation('Дождь', 0)
        >>> weather.rain_today()
        """

    ...



import doctest

if __name__ == "__main__":
    doctest.testmod() # TODO работоспособность экземпляров класса проверить с помощью doctest
pass
