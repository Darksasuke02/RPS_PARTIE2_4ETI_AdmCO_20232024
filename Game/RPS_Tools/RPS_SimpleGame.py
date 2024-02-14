from RPS_Game import RockPaperScissors
import time
class RPS_SimpleGame_class :
    def __init__(self, P1=None, P2=None):
        self.P1=P1
        self.P2=P2

    def SimplegameOneplayer(self):
        rps_game = RockPaperScissors(False, self.P1, self.P2)
        rps_game.play_rps()
        rps_game.check_play_status()
        self.SimplegameOneplayer()

    def SimplegameTwoplayers(self) :
        rps_game2v2 = RockPaperScissors(True, self.P1, self.P2)
        rps_game2v2.play_rps()
        rps_game2v2.check_play_status()
        self.SimplegameTwoplayers()

if __name__ == '__main__':
    partiesolo=RPS_SimpleGame_class('R','P')
    partiesolo.SimplegameTwoplayers()
 

