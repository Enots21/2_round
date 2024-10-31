import os
import time

for i in os.walk('..'):  # вывод списка файлов в директории
    print(i)

import os

path1 = "folder1"
path2 = "folder2"
path3 = "file.txt"
result = os.path.join(path1, path2, path3)
print(result)  # Вывод: folder1/folder2/file.txt

for root, dirs, files in os.walk('.'):
    for file in files:
        filepath = os.getcwd()
        filetime = os.path.getmtime('modyle7.py')
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize('modyle7.py')
        parent_dir = os.path.dirname('modyle7.py')
        print(
            f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
