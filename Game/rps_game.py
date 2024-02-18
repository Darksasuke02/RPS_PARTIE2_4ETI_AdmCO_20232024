"""
RPS module de jeu
Module qui permet de jouer de traiter les manches de pierre feuille ciseaux
"""

import random
import re
import os
import sys


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
                choices = ["R", "P", "S"]
                opp_choice = random.choice(choices)

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
