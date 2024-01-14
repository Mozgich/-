# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Ball:
    def __init__(self, size: int, weight: int):
        """
        Создание и подготовка к работе объекта "Мяч"

        :param size: размер мяча
        :param weight: вес мяча

        Примеры:
        >>> ball = Ball(5, 450)  # инициализация экземпляра класса
        """
        if not isinstance(size, int):
            raise TypeError("размер мяча должен быть типа int")
        if size < 0:
            raise ValueError("размер мяча должен быть положительным числом")
        self.size = size

        if not isinstance(weight, int):
            raise TypeError("вес мяча должен быть типа int")
        if weight < 0:
            raise ValueError("вес мяча должен быть положительным числом")
        self.weight = weight
    def deflated_ball(self) -> bool:
        """
        Функция, которая проверяет является ли мяч спущенным

        :return: Является ли спущенным

        примеры:
        >>> ball = Ball(5,450)
        >>> ball.deflated_ball()
        """
        ...
    def reduction_weight(self, new_weight: int) -> None:
        """
        Уменьшение веса мяча

        :param new_weight: Вес мяча, на который надо уменьшить
        :raise ValueError: Если уменьшенный вес больше, чем первоначальный

        Примеры:
        >>> ball = Ball(5,450)
        >>> ball.reduction_weight(40)
        """
        if not isinstance(new_weight, int):
            raise TypeError("Добавляемый вес должен быть типа int")
        if new_weight < 0:
            raise ValueError("Уменьшаемый вес должен быть положительным числом")
        ...


class Aeroplane:
    def __init__(self, max_motor_power: int, speed: (int,float)):
        """
        Создание и подготовка к работе объекта "Самолет"

        :param max_motor_power: максимальная мощность двигаетеля
        :param speed: скорость самолета

        Примеры:
        >>> aeroplane = Aeroplane(80, 800)  # инициализация экземпляра класса
        """
        if not isinstance(max_motor_power, int):
            raise TypeError("Мощность двигателя должна быть типа int")
        if max_motor_power < 0:
            raise ValueError("Мощность двигателя должна быть положительным числом")
        self.max_motor_power = max_motor_power

        if not isinstance(speed, (int, float)):
            raise TypeError("скорость самолета должна быть типа int или float")
        if speed < 0:
            raise ValueError("скорость самолета должна быть положительным числом")
        self.speed = speed

    def power_reduction_aeroplan(self, power) -> None:
        """
        Уменьшение мощности двигателя самолета
        :param power: Убавленная мощность

        примеры:
        >>> aeroplane = Aeroplane(20,800)
        >>> aeroplane.power_reduction_aeroplan(60)
        """
        ...
    def increase_speed(self, new_speed: (int,float)) -> None:
        """
        Увеличение скорости самолета
        :param new_speed: Увеличенная скорость

        :raise ValueError: Если увеличенная скорость меньше нуля

        Примеры:
        >>> aeroplane = Aeroplane(80,800)
        >>> aeroplane.power_reduction_aeroplan(100)
        """
        if not isinstance(new_speed, (int,float)):
            raise TypeError("Увеличенная скорость должна быть типа int")
        if new_speed < 0:
            raise ValueError("Увеличенная скорость должна быть положительным числом")
        ...
class Classroom:
    def __init__(self, number_of_seats: int, wall_colour: str):
        """
        Создание и подготовка к работе объекта "Aудитория"

        :param number_of_seats: количество мест в аудитории
        :param wall_colour: цвет стен

        Примеры:
        >>> classroom = Classroom(32, "Серый")  # инициализация экземпляра класса
        """
        if not isinstance(number_of_seats, int):
            raise TypeError("Количество мест в аудитории должно быть типа int")
        if number_of_seats < 0:
            raise ValueError("Количество мест в аудитории должно быть положительным числом")
        self.number_of_seats = number_of_seats

        if not isinstance(wall_colour, str):
            raise TypeError("цвет стен должен быть типа str")
        self.wall_colour = wall_colour

    def increase_number_of_seats(self, seats: int) -> None:
        """
        Увеличение количества мест в ауитории
        :param seats: Добавленные места

        примеры:
        >>> classroom = Classroom(35,"Серый")
        >>> classroom.increase_number_of_seats(3)
        """
        ...
    def wall_painting(self, new_colour: str) -> None:
        """
        Покраска стен
        :param new_colour: новый цвет стен


        Примеры:
        >>> classroom = Classroom(35,"Серый")
        >>> classroom.wall_painting("Белый")
        """
        if not isinstance(new_colour, str):
            raise TypeError("Цвет стен должен быть типа str")
        ...

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
    pass
