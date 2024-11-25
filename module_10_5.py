from datetime import datetime
import multiprocessing


def read_info(name):  # Создайте функцию read_info(name), где name - название файла
    all_data = []  # Создаем список
    with open(name) as files:  # Открываем файл
        while True:  # Пока файл не закончится
            lstk = files.readline().split()  # Считываем строку
            all_data.append(lstk)  # Добавляем строку в список
            if not lstk:  # Если строка пустая
                break  # stop


files = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']  # Список файлов
start_file = datetime.now()
for name in files:  # Для каждого файла
    print(name)
    read_info(name)  # Вызываем функцию

end_file = datetime.now()  # Создаем переменную для
time_of_line_function = end_file - start_file  # Вычисляем время работы линейного

print(f'Время работы линейного вызова : {time_of_line_function}')  # Выводим время работы

if __name__ == '__main__':
    start2 = datetime.now()

    with multiprocessing.Pool(processes=4) as pool:  # Создаем процессор
        pool.map(read_info, files)  # Вызываем функцию

    end2 = datetime.now()  # Создаем переменную для
    time_of_multiprocessing = end2 - start2  # Вычисляем время работы мультипр
    print(f'Время работы мультипроцесса : {time_of_multiprocessing}')  # Выводим время работы
