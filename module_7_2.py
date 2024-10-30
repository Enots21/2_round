import io
from pprint import pprint
strings = ['Text for tell.',
               'Используйте кодировку utf-8.',
               'Because there are 2 languages!',
               'Спасибо!']

def custom_write(file_name, strings):
    n = 0
    elem = {}
    for i in strings:
        file = open(file_name, 'a', encoding='utf-8')
        tell = file.tell()
        n += 1
        file.write(f'{i}\n')
        file.close()
        elem.update({(n, tell): i})
    return elem

result = custom_write('test.txt', strings)
for elem in result.items():
    print(elem)
