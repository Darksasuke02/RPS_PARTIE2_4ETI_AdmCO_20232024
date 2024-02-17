from RPS_Game import RockPaperScissors

'''
Classe qui permet la gestion des parties
'''
class RPS_SimpleGame_class :   
    '''
    Constructeur de la classe
    Entrées :
    P1 : facultatif choix du joueur 1
    P2 : facultatif choix du joueur 2
    '''
    def __init__(self, P1=None, P2=None):
        if P1.lower() not in ["r", "p", "s"]:
            P1=None
        elif P2.lower() not in ["r", "p", "s"]:
            P2=None
        self.P1=P1
        self.P2=P2

    '''
    Méthode récursive qui permet de gérer les parties contre l'ordinateur, s'arrete après avoir rentré No quand on nous demande si on veux rejouer
    '''
    def SimplegameOneplayer(self):
        rps_game = RockPaperScissors(False, self.P1, self.P2)
        rps_game.play_rps()
        rps_game.check_play_status()
        self.SimplegameOneplayer()

    '''
    Méthode récursive qui permet de gérer les parties à deux joueurs
    '''
    def SimplegameTwoplayers(self) :
        rps_game2v2 = RockPaperScissors(True, self.P1, self.P2)
        rps_game2v2.play_rps()
        rps_game2v2.check_play_status()
        self.SimplegameTwoplayers()

if __name__ == '__main__':
    partiesolo=RPS_SimpleGame_class('S','P')
    partiesolo.SimplegameTwoplayers()
 

