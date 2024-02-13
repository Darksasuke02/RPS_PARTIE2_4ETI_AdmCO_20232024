import random
import re
import os


class RockPaperScissors:
    def __init__(self, twoplayers):
        self.valid_responses = ['yes', 'no']
        self.twoplayers=twoplayers

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


    def play_rps(self):
        play = True
        while play:
            
            print('')
            print('Rock, Paper, Scissors - Shoot!')

            user_choice = input('Choose your weapon P1'
                              ' [R]ock], [P]aper, or [S]cissors: ')


            if not re.match("[SsRrPp]", user_choice):
                print('Please choose a letter:')
                print('[R]ock, [P]aper, or [S]cissors')
                continue

            print(f'You chose: {user_choice}')

            if self.twoplayers :
                opp_choice = input('Choose your weapon P1'
                              ' [R]ock], [P]aper, or [S]cissors: ')


                if not re.match("[SsRrPp]", opp_choice):
                    print('Please choose a letter:')
                    print('[R]ock, [P]aper, or [S]cissors')
                    continue
            else :    
                choices = ['R', 'P', 'S']
                opp_choice = random.choice(choices)

                print(f'I chose: {opp_choice}')
            
            if opp_choice == user_choice:
                print('Tie!')
                play = self.check_play_status()
            elif opp_choice == 'R' and user_choice == 'S':
                print('Rock beats scissors, I win!')
                play = self.check_play_status()
            elif opp_choice == 'S' and user_choice == 'P':
                print('Scissors beats paper! I win!')
                play = self.check_play_status()
            elif opp_choice == 'P' and user_choice == 'R':
                print('Paper beats rock, I win!')
                play = self.check_play_status()
            else:
                print('You win!\n')
                play = self.check_play_status()

