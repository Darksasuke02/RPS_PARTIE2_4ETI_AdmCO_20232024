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

    def simplegameoneplayer(self, sauv, nom=None):
        """
        Méthode récursive qui permet de gérer les parties contre l'ordinateur,
        s'arrete après avoir rentré No quand on nous demande si on veux rejouer
        """
        rps_game = RockPaperScissors(False, self.player_1, self.player_2)
        data = rps_game.play_rps()
        if sauv:
            gestionnaire.ajouter_contenu(nom + ":" + str(data[0]) + "," + data[1])
        rps_game.check_play_status()
        self.simplegameoneplayer(sauv, nom)

    def simplegametwoplayers(self):
        """
        Méthode récursive qui permet de gérer les parties à deux joueurs
        """
        rps_game2v2 = RockPaperScissors(True, self.player_1, self.player_2)
        rps_game2v2.play_rps()
        rps_game2v2.check_play_status()
        self.simplegametwoplayers()


class RPSMultipleGame:
    """
    Classe qui permet de traiter l'initialisation: le login et le lancement
    des parties contre l'ordinateur sauvegardées ou non
    """

    def login(self):
        """
        Méthode principale qui gère le login et l'initialisation des paties contre
        l'ordinateur.
        """
        nom = input("Rentrez votre pseudo :")
        reponses = ["yes", "no"]
        while True:
            try:
                gestion_cookies = input("Aimez-vous les cookies ? (yes or no) ")
                if gestion_cookies.lower() not in reponses:
                    raise ValueError("yes or no only")

                if gestion_cookies.lower() == "yes":
                    partiesolo = RPSSimpleGameclass()
                    partiesolo.simplegameoneplayer(True, nom)

                if gestion_cookies.lower() == "no":
                    partiesolo = RPSSimpleGameclass()
                    partiesolo.simplegameoneplayer(False)

            except ValueError as errorformat:
                print(errorformat)


class GestionFichier:
    """
    Classe qui regroupe les méthodes qui agissement sur le traitement des fichier
    de sauvegarde des data
    """

    def __init__(self, nom_fichier):
        """
        Contructeur de ma classe qui permet l'initialisation du fichier a modifier
        """
        self.nom_fichier = nom_fichier

    def ajouter_contenu(self, contenu):
        """
        Méthode qui permet de ajouter du contenu dans un fichier sous forme de append,
        saut de ligne à chaque fois
        """
        try:
            with open(self.nom_fichier, "a", encoding="utf-8") as fich:
                fich.write(contenu + "\n")
            print("Contenu ajouté avec succès au fichier", self.nom_fichier)
        except IOError as gestionfich:
            raise IOError(
                "Erreur : Impossible d'écrire dans le fichier", self.nom_fichier
            ) from gestionfich


if __name__ == "__main__":
    gestionnaire = GestionFichier("maches_jouées.txt")
    mode_de_jeu = ["ordi", "1v1"]
    while True:
        try:
            response = input("Quel mode de jeux 1v1 ou ordi ")
            if response.lower() not in mode_de_jeu:
                raise ValueError("ordi or 1v1 only")

            if response.lower() == "ordi":
                rps_login = RPSMultipleGame()
                rps_login.login()

            if response.lower() == "1v1":
                partiea2 = RPSSimpleGameclass()
                partiea2.simplegametwoplayers()

        except ValueError as err:
            print(err)
