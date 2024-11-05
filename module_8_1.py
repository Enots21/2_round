def add_everything_up(a, b):
    try:
       return round(a + b, 3) # вычисляем точность
    except TypeError:
        return str(a) + str(b) # возвращаем строку





print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))