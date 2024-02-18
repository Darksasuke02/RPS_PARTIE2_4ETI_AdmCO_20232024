"""
Module de test de notre pierre feuille ciseaux
"""
import unittest
from unittest.mock import patch
from rps_game import RockPaperScissors





class Testop(unittest.TestCase):
    """
    Classe de test unitest qui permet le test de notre jeu
    """

    def setUp(self):
        """
        Classe d'initialisation de nos test création de nos parties ou morceaux de parties
        """
        self.partiesolo = RockPaperScissors(False)
        self.partiemulti1 = RockPaperScissors(False, "R", "R")
        self.partiemulti2 = RockPaperScissors(False, "P", "R")
        self.partiemulti3 = RockPaperScissors(False, "S", "R")



    @patch("builtins.input", side_effect=["R", "P", "S"])
    def test_simple_play_rps(self, mock_input):
        """
        Méthode de test de play_rps
        """
        # Test de la 1 joueur
        answer1 = False
        answer2 = False
        answer3 = False
        result1 = self.partiesolo.play_rps()
        result2 = self.partiesolo.play_rps()
        result3 = self.partiesolo.play_rps()

        if result1 in (0, 1, 2):
            answer1 = True
        if result2 in (0, 1, 2):
            answer2 = True
        if result3 in (0, 1, 2):
            answer3 = True

        self.assertEqual(True, answer1)
        self.assertEqual(True, answer2)
        self.assertEqual(True, answer3)

        # Test de la 2v2
        result4 = self.partiemulti1.play_rps()
        result5 = self.partiemulti2.play_rps()
        result6 = self.partiemulti3.play_rps()

        self.assertEqual(result4, 0)
        self.assertEqual(result5, 1)
        self.assertEqual(result6, 2)


if __name__ == "__main__":
    unittest.main()
raise ValueError("Mauvais Fake Input Player 1")