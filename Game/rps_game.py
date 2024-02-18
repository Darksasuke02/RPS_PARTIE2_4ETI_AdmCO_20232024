"""
RPS module de jeu
Module qui permet de jouer de traiter les manches de pierre feuille ciseaux
"""

import random
import re
import os
import sys
import linecache


class RockPaperScissors:

    """
    Classe qui permet de gérer les méthodes classique du jeux
    """

    def __init__(self, twoplayers, player_1=None, player_2=None):
        """
        Constructeur de ma classe
        Entrée :
            twoplayers : bool qui détermine le type de la partie
            player_1 : facultatif Choix du playeur 1 (input sinon)
            player_2 : facultatif Choix du joueur 2 (input sinon)
        """
        self.valid_responses = ["yes", "no"]
        self.twoplayers = twoplayers
        self.player_1 = player_1
        self.player_2 = player_2
        self.tableau = []

    def check_play_status(self):
        """
        Classe qui permet de gérer le relancement de la partie selon l'input utilisateur,
        yes-ralance no-arrete et clear la console
        """
        valid_responses = ["yes", "no"]
        while True:
            try:
                response = input("Do you wish to play again? (Yes or No): ")
                if response.lower() not in valid_responses:
                    raise ValueError("Yes or No only")

                if response.lower() == "yes":
                    return True
                else:
                    os.system("cls" if os.name == "nt" else "clear")
                    print("Thanks for playing!")
                    sys.exit()

            except ValueError as err:
                print(err)

    def play_rps(self):
        """
        classe qui permet de gérer les maches à la fois les inputs utilisateur,
        (génère le choix ordi si nécessaire) et détermine le gagnant
        """
        play = True
        while play:

            print("")
            print("Rock, Paper, Scissors - Shoot!")
            user_choice = self.player_1
            opp_choice = self.player_2

            if user_choice is None:
                user_choice = input(
                    "Choose your weapon player_1" " [R]ock], [P]aper, or [S]cissors: "
                )

            if not re.match("[SsRrPp]", user_choice):
                print("Please choose a letter:")
                print("[R]ock, [P]aper, or [S]cissors")
                continue

            print(f"You chose: {user_choice}")

            if self.twoplayers and opp_choice is None:
                opp_choice = input(
                    "Choose your weapon player_2" " [R]ock], [P]aper, or [S]cissors: "
                )

                if not re.match("[SsRrPp]", opp_choice):
                    print("Please choose a letter:")
                    print("[R]ock, [P]aper, or [S]cissors")
                    continue
            elif opp_choice is None:
                self.creation_tableau()
                if self.tableau == []:
                    choices = ["R", "P", "S"]
                    opp_choice = random.choice(choices)

                else:
                    ponderation = self.strat1()
                    choix = ["R", "P", "S"]
                    opp_choice = random.choices(choix, weights=ponderation)[0]

                print(f"I chose: {opp_choice}")

            if opp_choice == user_choice:
                print("Tie!")
                return (0, user_choice)
            elif opp_choice == "R" and user_choice == "S":
                print("Rock beats scissors, player_2 (or robot) win!")
                return (2, user_choice)
            elif opp_choice == "S" and user_choice == "P":
                print("Scissors beats paper! player_2 (or robot) win!")
                return (2, user_choice)
            elif opp_choice == "P" and user_choice == "R":
                print("Paper beats rock, player_2 (or robot) win!")
                return (2, user_choice)
            else:
                print("player_1 win !\n")
                return (1, user_choice)

    def creation_tableau(self):
        """
        Cette méthode se sert du fichier des parties jouer pour en créer
        un tableau, facilement exploitables dans les méthodes de
        stratégie.
        """
        chemin_fichier = "manches_jouees.txt"
        if os.path.isfile(chemin_fichier):
            # Lecture du fichier
            with open(chemin_fichier, "r", encoding="utf-8") as file:
                contenu = file.readlines()

            if self.tableau == []:
                # Initialisation du tableau
                compteur = 0
                # Traitement de chaque ligne du fichier
                for ligne in contenu:

                    self.tableau.append([])
                    partie_deux_points = ligne.strip().split(":")[1]
                    # Supprimer les caractères de saut de ligne et
                    # diviser la ligne en fonction du délimiteur ","
                    elements1 = partie_deux_points.strip().split(",")[1] 
                    # Prendre seulement la partie après le délimiteur ":"
                    elements2 = partie_deux_points.strip().split(",")[0]
                    # Ajouter les éléments au tableau
                    self.tableau[compteur].append(elements2)
                    self.tableau[compteur].append(elements1)
                    compteur = compteur + 1

                    # Afficher le tableau
                    # print(self.tableau)

            else:
                valeur_dern_ligne = len(self.tableau) + 1
                dernière_ligne = linecache.getline(
                    chemin_fichier, len(self.tableau) + 1
                )
                self.tableau.append([])
                partie = dernière_ligne.strip().split(":")[1]
                # Recupérer la partie après les :
                elements1 = partie.strip().split(",")[1]
                # Récupérer la partie après
                elements2 = partie.strip().split(",")[0]
                # Récupérer la partie avant
                self.tableau[valeur_dern_ligne].append(elements2)
                self.tableau[valeur_dern_ligne].append(elements1)

        else:
            print("Le fichier spécifié n'existe pas.")
        return self.tableau

    def strat1(self):
        """
        Méthode qui gère la stratégie de l'ordi en partie player contre machine
        Elle regardes la stratégie des utilisateurs (sans regarder le login name)
        Elle renvoie une pondération permettant d'améliorer le choix de l'ordi
        Il y a inversement des R, P et S et c'est normal (si R sort beaucoup il faut jouer P)
        Sorties :
            Liste pondération : [R, P, S]
        """
        comptages = {"R": 0, "P": 0, "S": 0}
        for i in range(len(self.tableau)):
            # Accéder à la deuxième lettre de l'élément et l'incrémenter dans le dictionnaire
            comptages[self.tableau[i][1]] += 1

        print("Nombre de 'R' :", comptages["R"])
        print("Nombre de 'P' :", comptages["P"])
        print("Nombre de 'S' :", comptages["S"])
        ponderation = [comptages["S"], comptages["R"], comptages["P"]]
        return ponderation


