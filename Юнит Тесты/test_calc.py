import calc as rnt
import unittest

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}#{'Усэйн': 10, 'Андрей': 9, 'Ник': 3}

    def setUp(self):
        vs = {'Усэйн': 10, 'Андрей': 9, 'Ник': 3}#
        self.runners = {n: rnt.Runner(name=n, speed=v) for n, v in vs.items()}# Считыватель дистанций

    @classmethod
    def tearDownClass(cls):#Завершение теста
        for k, v in cls.all_results.items():
            print(f'{k}: {v}')

    def test_tournament(self):#Тестирование
        tour = rnt.Tournament(90, self.runners['Усэйн'], self.runners['Ник'])
        all_results = tour.start()
        self.assertTrue(all_results[2], self.runners['Ник'])

    def test_tournament_2(self):#Тестирование
        tour = rnt.Tournament(90, self.runners['Андрей'], self.runners['Ник'])
        all_results = tour.start()
        self.assertTrue(all_results[2], self.runners['Ник'])

    def test_tournament_3(self):#Тестирование
        tour = rnt.Tournament(90, self.runners['Усэйн'], self.runners['Андрей'], self.runners['Ник'])
        all_results = tour.start()
        self.assertTrue(all_results[3], self.runners['Ник'])

if __name__ == '__main__':
    unittest.main()
