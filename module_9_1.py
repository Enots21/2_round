def apply_all_func(int_list, *functions):  # Функция
    results = {}# Создание словаря
    for func in functions:#Цикл
        results[func.__name__] = func(int_list)#Вызов функции
    return results#Возврат результата


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
#[Александров Даниил Сергеевич]
#module_9_1.py
