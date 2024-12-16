class Runner:
    """
    класс спортсменов по бегу
    принимает параметры: имя и скорость(по умолчанию 5)
    обладает методом run(увеличивает дистанцию в два раза по сравнению со скоростью)
    и методом walk(увеличивает дистанцию на величину скорости), а также магическими методами __str__ и __eq__
    для вывода имени спортсмена и сравнении имён спортсменов(бегунов)
    """

    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    """
    Класс для проведения забега.
        Принимает на вход дистанцию и участников.
        Метод start() запускает забег.

    """

    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        """
        Исправленный метод запускает забег.
        :return: Словарь с финишировавшими участниками
        """
        finishers = {}
        place = 1
        remaining_participants = self.participants[:]  # список участников

        while remaining_participants:  # while пока есть участники
            new_remaining_participants = []  # новый список участников

            for participant in remaining_participants:  # проходимся по списку участников
                participant.run()  # Стартует каждый из участников

                if participant.distance >= self.full_distance:  # если участник достиг максимальной дистанции
                    finishers[place] = participant  # добавляем его в список финишировавших
                    place += 1  # увеличиваем номер места
                else:
                    new_remaining_participants.append(participant)  # если участник не достиг максимальной
                    # дистанции добавляем его в новый список участников

            remaining_participants = new_remaining_participants  # обновляем список участников

        return finishers

# старый код    # finishers = {}
# place = 1
# while self.participants:
#     for participant in self.participants:
#         participant.run()
#         if participant.distance >= self.full_distance:
#             finishers[place] = participant
#             place += 1
#             self.participants.remove(participant)
#
# return finishers
