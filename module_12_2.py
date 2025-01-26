import runner_and_tournament
import unittest

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
    def setUp(self):
        self.setup_1 = runner_and_tournament.Runner('Усэйн', 10)
        self.setup_2 = runner_and_tournament.Runner('Андрей', 9)
        self.setup_3 = runner_and_tournament.Runner('Ник', 3)
    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            show_result = {}
            for place, runner in result.items():
                show_result[place] = runner.name
            print(show_result)
    def test_run_1(self):
        self.tnm_1 = runner_and_tournament.Tournament(90, self.setup_1, self.setup_3)
        self.all_results = self.tnm_1.start()
        last_result = max(self.all_results)
        self.assertTrue(last_result != 'Ник')
        TournamentTest.all_results[1] = self.all_results
    def test_run_2(self):
        self.tnm_2 = runner_and_tournament.Tournament(90, self.setup_2, self.setup_3)
        self.all_results = self.tnm_2.start()
        last_result = max(self.all_results)
        self.assertTrue(last_result != 'Ник')
        TournamentTest.all_results[2] = self.all_results
    def test_run_3(self):
        self.tnm_3 = runner_and_tournament.Tournament(90, self.setup_1, self.setup_2,
                                                        self.setup_3)
        self.all_results = self.tnm_3.start()
        last_result = max(self.all_results)
        self.assertTrue(last_result != 'Ник')
        TournamentTest.all_results[3] = self.all_results

if __name__ == '__main__':
    unittest.main()