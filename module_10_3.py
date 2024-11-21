import threading
import time
from random import randint


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            rand_num = randint(50, 500)
            with self.lock:  # Если баланс больше или равен 500 и замок lock
                if self.balance < 500 and self.lock.locked():
                    self.balance += rand_num
                    print(f"Пополнение: {rand_num}. Баланс: {self.balance}")
            time.sleep(0.001)  # скорость выполнения

    def take(self):
        for i in range(100):
            rand_nums = randint(50, 500)
            print(f"Запрос на {rand_nums}")
            with self.lock:  #вызов lock
                if rand_nums <= self.balance:
                    self.balance -= rand_nums
                    print(f"Снятие: {rand_nums}. Баланс: {self.balance}")
                    time.sleep(0.001)  # скорость выполнения
                else:
                    print("Запрос отклонён, недостаточно средств")
            time.sleep(0.001)  # скорость выполнения


bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
