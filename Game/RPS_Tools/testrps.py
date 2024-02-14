from RPS_Game import RockPaperScissors

from RPS_SimpleGame import RPS_SimpleGame_class


import unittest
from unittest.mock import patch

class Testop(unittest.TestCase):
    def setUp(self):
        self.partiesolo=RockPaperScissors(False)
        self.partiegen=RockPaperScissors(False)




    @patch('builtins.input', side_effect=['R', 'P', 'S'])
    def test_simple_play_rps(self, mock_input):
        answer1=False
        answer2=False
        answer3=False
        result1=self.partiesolo.play_rps()
        result2=self.partiesolo.play_rps()
        result3=self.partiesolo.play_rps()
        if result1 == 0 or result1 == 1 or result1 == 2 :
            answer1=True
        if result2 == 0 or result2 == 1 or result2 == 2 :
            answer2=True
        if result3 == 0 or result3 == 1 or result3 == 2 :
            answer3=True
        self.assertEqual(True, answer1)
        self.assertEqual(True, answer2)
        self.assertEqual(True, answer3)

    





if __name__ == '__main__':
    unittest.main()




