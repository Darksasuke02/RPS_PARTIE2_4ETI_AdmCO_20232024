from RPS_Game import *


class RPS_SimpleGame_class :

    def SimplegameOneplayer(self):
        rps_game = RockPaperScissors(False)
        rps_game.play_rps()
    
    def SimplegameTwoplayers(self) :
        rps_game2v2 = RockPaperScissors(True)
        rps_game2v2.play_rps()

 
 


if __name__ == '__main__':
    partiesolo=RPS_SimpleGame_class()
    partiesolo.SimplegameTwoplayers()
 

