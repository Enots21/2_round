class Animal:
    def __init__(self, name):
        self.alive = True # Перед аlive надо вставить self
        self.fed = False # Перед fed надо вставить self
        self.name = name

    def eat(self, food):
        self.food = food #Перед food надо вставить self

        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False


class Mammal(Animal):
    pass

class Predator(Animal):
    pass



class Plant:
    def __init__(self, name):
        self.edible = False #Перед edible надо вставить self
        self.name = name

class Flower(Plant):
    pass

class Fruit(Plant):
    def __init__(self, name):
        self.edible = True #Перед dible надо вставить self
        self.name = name
#
#
#






a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name) #Работает
print(p1.name)  #Работает

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)

# Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.
