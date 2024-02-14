from RPS_Game import RockPaperScissors


class RPS_SimpleGame_class :

    def SimplegameOneplayer(self):
        rps_game = RockPaperScissors(False)
        rps_game.play_rps()
        rps_game.check_play_status()
        self.SimplegameOneplayer()

    def SimplegameTwoplayers(self) :
        rps_game2v2 = RockPaperScissors(True)
        rps_game2v2.play_rps()
        rps_game2v2.check_play_status()
        self.SimplegameTwoplayers()

if __name__ == '__main__':
    partiesolo=RPS_SimpleGame_class()
    partiesolo.SimplegameOneplayer()
 

