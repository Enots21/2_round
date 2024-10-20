# Цель: понять как работают базовые магические методы на практике.
#
# Задача "Магические здания":
# Для решения этой задачи будем пользоваться решением к предыдущей задаче "Атрибуты и методы объекта".
#
# Необходимо дополнить класс House следующими специальными методами:
# __len__(self) - должен возвращать кол-во этажей здания self.number_of_floors.
# __str__(self) - должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>".

# Цель: понять разницу между атрибутами объекта и класса,
# дополнив уже существующий класс. Применить метод __new__.
#
# Дополнительно о работе метода __new__:

class House:  # Class
    houses_history = []  # List

    def __new__(cls, *args, **kwargs):  # Функция которая добовляет в список даннные
        obj = object.__new__(cls)  #
        cls.houses_history.append(args[0])  #
        return obj  #

    def __init__(self, name, floors):  #
        self.name = name  #
        self.floors = floors  #
        setattr(self, name, floors)  #

    def __del__(self):  # функция которая удаляет
        print(f'{self.name} снесён, но он останется в истории')


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)

#
# Вывод на консоль:
# ['ЖК Эльбрус']
# ['ЖК Эльбрус', 'ЖК Акация']
# ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']
# ЖК Акация снесён, но он останется в истории
# ЖК Матрёшки снесён, но он останется в истории
# ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']
# ЖК Эльбрус снесён, но он останется в истории