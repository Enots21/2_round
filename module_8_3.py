# Задача "Некорректность"
class IncorrectVinNumber(Exception):  # Некорректный VIN
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class IncorrectCarNumbers(Exception):  # Некорректный Number
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class Car:  # класс
    def __init__(self, model, vin, numbers):  # конструктор
        self.model = model  # Модель
        if self.__is_valid_vin(vin):  # Валидация VIN
            self.__vin = vin
        if self.__is_valid_numbers(numbers):  # Валидация номеров
            self.__numbers = numbers

    def __is_valid_vin(self, vin_number):  # Валидация VIN
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        elif not (1000000 <= vin_number <= 9999999):
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return True

    def __is_valid_numbers(self, numbers):  # метод#Валидация номеров
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        elif len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        return True


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')
