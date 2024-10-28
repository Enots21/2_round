# Подробное ТЗ:
#
# Атрибуты класса Figure: sides_count = 0
# Каждый объект класса Figure должен обладать следующими атрибутами:
# Атрибуты(инкапсулированные): __sides(список сторон (целые числа)), __color(список цветов в формате RGB)
# Атрибуты(публичные): filled(закрашенный, bool)
# И методами:
# Метод get_color, возвращает список RGB цветов.
# Метод __is_valid_color - служебный, принимает параметры r, g, b, который проверяет корректность переданных значений перед установкой нового цвета. Корректным цвет: все значения r, g и b - целые числа в диапазоне от 0 до 255 (включительно).
# Метод set_color принимает параметры r, g, b - числа и изменяет атрибут __color на соответствующие значения, предварительно проверив их на корректность. Если введены некорректные данные, то цвет остаётся прежним.
# Метод __is_valid_sides - служебный, принимает неограниченное кол-во сторон, возвращает True если все стороны целые положительные числа и кол-во новых сторон совпадает с текущим, False - во всех остальных случаях.
# Метод get_sides должен возвращать значение я атрибута __sides.
# Метод __len__ должен возвращать периметр фигуры.
# Метод set_sides(self, *new_sides) должен принимать новые стороны, если их количество не равно sides_count, то не изменять, в противном случае - менять.
#
# Атрибуты класса Circle: sides_count = 1
# Каждый объект класса Circle должен обладать следующими атрибутами и методами:
# Все атрибуты и методы класса Figure
# Атрибут __radius, рассчитать исходя из длины окружности (одной единственной стороны).
# Метод get_square возвращает площадь круга (можно рассчитать как через длину, так и через радиус).
#
# Атрибуты класса Triangle: sides_count = 3
# Каждый объект класса Triangle должен обладать следующими атрибутами и методами:
# Все атрибуты и методы класса Figure
# Метод get_square возвращает площадь треугольника. (можно рассчитать по формуле Герона)
# Атрибуты класса Cube: sides_count = 12
# Каждый объект класса Cube должен обладать следующими атрибутами и методами:
# Все атрибуты и методы класса Figure.
# Переопределить __sides сделав список из 12 одинаковы сторон (передаётся 1 сторона)
# Метод get_volume, возвращает объём куба.
#



from math import pi, sqrt


class Figure:
  sides_count = 0  # Атрибут

  def __init__(self, color: tuple, *sides: int, filled: bool = True) -> None:
    #  -> None - указание типа возвращаемого значения
    if len(sides) != self.sides_count:
      self.__sides = [1 * self.sides_count]  # инкапсулированны [1]
    else:
      self.__sides = [i for i in sides]  # [1, 2, 3, 4]
    self.__color = color
    self.filled = filled

  def get_color(self):
    return list(self.__color)  # возвращаем список цветов
    # return [i for i in self.__color]

  def __is_valid_color(self, r, g, b) -> bool:
    """Проверка, что значения r, g, b от 0 до 255"""
    lst = [r, g, b]
    lst.sort()
    if lst[0] < 0 or lst[-1] > 255:
      return False
    else:
      return True

  def set_color(self, r, g, b):
    if self.__is_valid_color(r, g, b):
      self.__color = (r, g, b)

  def __is_valid_sides(self, sides: tuple) -> bool:
    res = []
    for i in sides:
      if i > 0:
        res.append(i)
    if len(res) > 0 and len(sides) == len(self.__sides):
      return True
    else:
      return False

  def set_sides(self, *sides):
    if self.__is_valid_sides(sides):
      self.__sides = sides

  def get_sides(self):
    return [*self.__sides]

  def __len__(self):
    return sum(self.__sides)


class Circle(Figure):
  sides_count = 1

  def __radius(self):
    return self.__len__ * (2 / pi)

  def get_square(self):
    return (self.__len__ ** 2) / (4 * pi)


class Triangle(Figure):
  sides_count = 3

  def get_square(self):
    sp = self.__len__ / 2
    s = sqrt(sp * (sp - self.__sides[0]) * (sp - self.__sides[1]) * (sp - self.__sides[2]))
    return s


class Cube(Figure):
  sides_count = 12

  def __init__(self, color, *sides: int, filled: bool = True):
    super().__init__(color, *sides, filled)
    if len(sides) == 1:
      self.__sides = self.sides_count * [i for i in sides]
    else:
      self.__sides = [1 * self.sides_count]

  def get_volume(self):
    return self.__sides[1] ** 3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())