# Цель: понять как работают базовые магические методы на практике.
#
# Задача "Магические здания":
# Для решения этой задачи будем пользоваться решением к предыдущей задаче "Атрибуты и методы объекта".
#
# Необходимо дополнить класс House следующими специальными методами:
# __len__(self) - должен возвращать кол-во этажей здания self.number_of_floors.
# __str__(self) - должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>".

class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        self.new_floor = 1

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __len__(self):
        return self.number_of_floors

    def __eq__(self, other):
        return isinstance(other, House) and self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    #
    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    #
    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    #
    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    #
    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    #
    def __add__(self, value):
        return House(self.name, self.number_of_floors + value)

    #
    #
    def __radd__(self, value):
        return House(self.name, self.number_of_floors + value)

    #
    #
    def __iadd__(self, value):
        return House(self.name, value + self.number_of_floors)


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(f'{str(h1)}')
print(f'{str(h2)}')

print(h1 == h2)  # __eq__
#
h1 = h1 + 10  # __add__
print(f'{str(h1)}')
print(h1 == h2)
#
h1 += 10  # __iadd__
print(h1)
#
h2 = 10 + h2  # __radd__
print(h2)
#
print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__
