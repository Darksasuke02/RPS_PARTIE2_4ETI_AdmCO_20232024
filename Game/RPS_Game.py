import random
import re
import os

'''
Classe qui permet de jouer de traiter les manches de pierre feuille ciseaux
'''
class RockPaperScissors:
    '''
    Constructeur de ma classe
    Entrée :
    twoplayers : bool qui détermine si la partie sera un 2v2, ou une partie contre l'ordinateur
    P1 : facultatif Choix du playeur 1  il sera demandé via une input si nous renseignée ici
    P2 : facultatif Choix du joueur 2 il sera demandé via une input si non renseignée
    '''
    def __init__(self, twoplayers, P1=None, P2=None):
        self.valid_responses = ['yes', 'no']
        self.twoplayers=twoplayers
        self.P1=P1
        self.P2=P2

    '''
    Classe qui permet de gérer le relancement de la partie selon l'input utilisateur yes-ralance no-arrete et clear la console
    '''
    def check_play_status(self):
        valid_responses = ['yes', 'no']
        while True:
            try:
                response = input('Do you wish to play again? (Yes or No): ')
                if response.lower() not in valid_responses:
                    raise ValueError('Yes or No only')

                if response.lower() == 'yes':
                    return True
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('Thanks for playing!')
                    exit()

            except ValueError as err:
                print(err)

    '''
    classe qui permet de gérer les maches à la fois les inputs utilisateur, (génère le choix ordi si nécessaire) et détermine le gagnant
    '''
    def play_rps(self):
        play = True
        while play:
            
            print('')
            print('Rock, Paper, Scissors - Shoot!')
            user_choice=self.P1
            opp_choice=self.P2
            
            if user_choice==None :
                user_choice = input('Choose your weapon P1'
                                ' [R]ock], [P]aper, or [S]cissors: ')


            if not re.match("[SsRrPp]", user_choice):
                print('Please choose a letter:')
                print('[R]ock, [P]aper, or [S]cissors')
                continue

            print(f'You chose: {user_choice}')

            if self.twoplayers and opp_choice==None :
                opp_choice = input('Choose your weapon P2'
                              ' [R]ock], [P]aper, or [S]cissors: ')


                if not re.match("[SsRrPp]", opp_choice):
                    print('Please choose a letter:')
                    print('[R]ock, [P]aper, or [S]cissors')
                    continue
            elif opp_choice==None :    
                choices = ['R', 'P', 'S']
                opp_choice = random.choice(choices)

                print(f'I chose: {opp_choice}')
            
            if opp_choice == user_choice :
                print('Tie!')
                return(0)
            elif opp_choice == 'R' and user_choice == 'S':
                print('Rock beats scissors, P2 (or robot) win!')
                return(2)
            elif opp_choice == 'S' and user_choice == 'P':
                print('Scissors beats paper! P2 (or robot) win!')
                return(2)
            elif opp_choice == 'P' and user_choice == 'R':
                print('Paper beats rock, P2 (or robot) win!')
                return(2)
            else:
                print('P1 win !\n')
                return(1)
                

