import threading  # Библиотеки
import time


class Knight(threading.Thread):  # Класс
    def __init__(self, name: str, power: int):  # Конструктор
        threading.Thread.__init__(self)  # Конструктор
        self.name = name  # Название
        self.power = power  # Мощность
        self.den = 0  # День
        self.voinov = 100  # Воинов

    def run(self):  # Метод
        print(f"{self.name}, на нас напали!")  # Вывод
        try:  # Попытка
            while self.voinov > 0:  # Цикл
                print(f'{self.name}, сражается день {self.den}(дня), осталось {self.voinov} воинов.')  # Вывод
                self.voinov -= self.power  # Уменьшение воинов
                self.den += 1  # День
                time.sleep(1)  # Задержка
        except:  # Попытка
            pass  # Нет
        finally:  # Конец
            print(f'{self.name} одержал победу спустя {self.den} дней(дня)!"')  # Вывод


# Создание класса
first_knight = Knight('Sir Lancelot', 10)  # Конструктор
second_knight = Knight("Sir Galahad", 20)  # Конструктор
# Запуск потоков и остановка текущего
# Вывод строки об окончании сражения
first_knight.start()  # Запуск потока
second_knight.start()  # Запуск потока

first_knight.join()  # Остановка потока
second_knight.join()  # Остановка потока

print('Все битвы закончились!')  # Вывод
