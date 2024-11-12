def all_variants(text):#Функция
    for i in range(1, len(text) + 1):#Перебираем все возможные
        for j in range(len(text) - i + 1):#Перебираем все возможные
            yield text[j:j + i]#Возвращаем результат

a = all_variants("abc")#Вызываем функцию
for combo in a:#Выводим результат
    print(combo)#Выводим


