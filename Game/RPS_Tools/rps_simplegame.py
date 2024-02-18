"""
Module qui traite la gestion des parties de pierre feuille ciseaux
"""



from rps_game import RockPaperScissors


class RPSSimpleGameclass:
    """
    Classe qui permet de traiter les différent type de partie,
    contre l'ordinateur ou 1v1
    """


    def __init__(self, player_1=None, player_2=None):
        """
        Constructeur de la classe
        Entrées :
            player_1 : facultatif choix du joueur 1
            player_2 : facultatif choix du joueur 2
        """
        if player_1 not in ["r", "p", "s", "R", "P", "S", None]:
            raise ValueError("Mauvais Fake Input Player 1")
        elif player_2 not in ["r", "p", "s", "R", "P", "S", None]:
            raise ValueError("Mauvais Fake Input Player 2")
        self.player_1 = player_1
        self.player_2 = player_2

    def simplegameoneplayer(self):
        """
        Méthode récursive qui permet de gérer les parties contre l'ordinateur,
        s'arrete après avoir rentré No quand on nous demande si on veux rejouer
        """
        rps_game = RockPaperScissors(False, self.player_1, self.player_2)
        rps_game.play_rps()
        rps_game.check_play_status()
        self.simplegameoneplayer()


    def simplegametwoplayers(self):
        """
        Méthode récursive qui permet de gérer les parties à deux joueurs
        """
        rps_game2v2 = RockPaperScissors(True, self.player_1, self.player_2)
        rps_game2v2.play_rps()
        rps_game2v2.check_play_status()
        self.simplegametwoplayers()

if __name__ == "__main__":
    mode_de_jeu = ["ordi", "1v1"]
    while True:
        try:
            response = input("Quel mode de jeux 1v1 ou ordi ")
            if response.lower() not in mode_de_jeu:
                raise ValueError("ordi or 1v1 only")

            if response.lower() == "ordi":
                partiesolo = RPSSimpleGameclass()
                partiesolo.simplegameoneplayer()

            if response.lower() == "1v1":
                partiea2 = RPSSimpleGameclass()
                partiea2.simplegametwoplayers()

        except ValueError as err:
            print(err)
