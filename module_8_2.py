def personal_sum(*numbers): #Функция personal sum n-ое число
    result = 0 #Создание переменной result
    incorrect_data = 0 #Создание переменной incorrect_data
    for i in numbers: #Перебор всех элементов списка
        for j in i: #Перебор каждого элемента списка
            try:#Попытка выполнить операцию
                result += j#Выполнение операции
            except TypeError:#Попытка выполнить операцию
                incorrect_data += 1#Выполнение операции
                print(f'некорректный тип данных для подсчета суммы - {j}')#Вывод ошибки
    return result, incorrect_data#Возвращение результата


def calculate_average(*numbers):#Функция calculate average n-ое число
    if isinstance(numbers, int):#Проверка на тип данных
        return None#Возвращение None
    try:#Попытка выполнить операцию
        tuple_sum = personal_sum(*numbers)#Выполнение операции
        return tuple_sum[0] / (len(*numbers) - tuple_sum[1])#Выполнение операции
    except ZeroDivisionError:#Попытка выполнить операцию
        return 0#Выполнение операции
    except TypeError:#Попытка выполнить операцию
        print(f'В numbers записан некорректный тип данных')#Вывод ошибки
        return None#Возвращение None


print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать



#[Александров Даниил Сергеевич]