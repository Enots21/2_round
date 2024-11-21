# Задача 1 (просто) "Арифметика":
# 1st program
def mas():
    max_sum = lambda a, b, c: c * (a ** b)
    max_sums = max_sum(9, 0.5, 5)
    print(max_sums)
mas()


# Задача 2 (просто) "Логика":
# 2st program
def gsc(a, b, c, d):
    if a > b and c != d:
        print(True)
    else:
        print(False)


gsc(9.99, 9.98, 1000, 1000.1)

# Задача 3 (средне) "Школьная загадка":
# 3st program
print(2 * 2 + 2 == 2 * (2 + 2))


#Задача 4 (сложно) "Первый после точки":
#4st program
sim = float('123.456')
print(sim*10)
print(int(sim*10)%10)
