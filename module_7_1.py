from pprint import pprint

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    def __init__(self):
        self.__file_name = open('products.txt', 'a')
        self.__file_name.close()

    def get_products(self):
        file = open('products.txt', 'r')
        name_prod = file.read()
        file.close()
        return name_prod

    def add(self, *products):
        for product in products:
            if str(product) not in self.get_products():
                file = open('products.txt', 'a+')
                file.write(f'{str(product)}\n')
                file.close()
            else:
                print(f'Продукт {product} уже есть в магазине')










#======================================================================
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())


#
# ========= ===============================================================
#  Значение символа
#  --------- ---------------------------------------------------------------
#  "r" открыть для чтения (по умолчанию)
#  "w" открыть для записи, предварительно обрезав файл
#  "x" создать новый файл и открыть его для записи
# "a" открыть для записи, добавив в конец файла, если он существует.
#  "b" двоичный режим
# "t" текстовый режим (по умолчанию)
#  "+" открыть файл на диске для обновления (чтения и записи)
#  "U" универсальный режим перевода строки (устарел)
#  ========= ============================================