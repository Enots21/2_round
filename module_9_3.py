first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(i) - len(s) for i, s in zip(first, second) if len(i) != len(s))
second_result = (len(first[n]) == len(second[n]) for n in range(len(first)))

print(list(first_result))
print(list(second_result))