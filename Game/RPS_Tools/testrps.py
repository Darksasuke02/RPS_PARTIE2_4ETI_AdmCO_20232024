"""
Module de test de notre pierre feuille ciseaux
"""
import unittest
from unittest.mock import patch
from rps_game import RockPaperScissors
from RPS_Tools.rps_simplegame import GestionFichier


class Testop(unittest.TestCase):
    """
    Classe de test unitest qui permet le test de notre jeu
    """

    def setUp(self):
        """
        Classe d'initialisation de nos test création de nos parties ou morceaux de parties
        """
        self.partiesolo = RockPaperScissors(False)
        self.partiemulti1 = RockPaperScissors(True, "R", "R")
        self.partiemulti2 = RockPaperScissors(True, "P", "R")
        self.partiemulti3 = RockPaperScissors(True, "S", "R")

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

        if result1[0] in (0, 1, 2):
            answer1 = True
        if result2[0] in (0, 1, 2):
            answer2 = True
        if result3[0] in (0, 1, 2):
            answer3 = True

        self.assertEqual(True, answer1)
        self.assertEqual(True, answer2)
        self.assertEqual(True, answer3)

        # Test de la 2v2
        result4 = self.partiemulti1.play_rps()
        result5 = self.partiemulti2.play_rps()
        result6 = self.partiemulti3.play_rps()

        self.assertEqual(result4[0], 0)
        self.assertEqual(result5[0], 1)
        self.assertEqual(result6[0], 2)

    def test_creation_ecriture(self):
        """
        Méthode de test de du gestionnaire de fichiers
        """
        gestionnaire = GestionFichier("test_file.txt")
        self.assertTrue(gestionnaire is not None)

        contenu_attendu = "Test d'écriture dans le fichier"
        gestionnaire.ajouter_contenu(contenu_attendu)

        with open("test_file.txt", "r", encoding="utf-8") as fich:
            contenu_reel = fich.read()

        self.assertEqual(contenu_attendu, contenu_reel[:-1])  # à cause du \n
        with open("test_file.txt", "w", encoding="utf-8"):
            pass


if __name__ == "__main__":
    unittest.main()
