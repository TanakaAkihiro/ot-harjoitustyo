import unittest
from repositories.score_repository import score_repository


class TestScoreRepository(unittest.TestCase):
    def setUp(self):
        score_repository.delete_all()
    
    def test_add_new_score(self):
        score_repository.add_new_score("Pekka", 100)
        score = score_repository.find_high_scores()

        self.assertEqual(len(score), 1)
        self.assertEqual((score[0][0], score[0][1]), ("Pekka", 100))
    
    def test_find_ranking(self):
        score_repository.add_new_score("Mikko", 10)
        score_repository.add_new_score("Paavo", 1)
        score_repository.add_new_score("Tiitu", 50)
        score = score_repository.find_high_scores()

        self.assertEqual(len(score), 3)
        self.assertEqual((score[0][0],score[0][1]), ("Tiitu", 50))
        self.assertEqual((score[1][0],score[1][1]), ("Mikko", 10))
        self.assertEqual((score[2][0],score[2][1]), ("Paavo", 1))
