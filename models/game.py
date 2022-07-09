import random

class Game:
    def __init__(self, _player1, _player2):
        self.player1 = _player1
        self.player2 = _player2
        self.player1_score = 0
        self.player2_score = 0

    def getResult(self):
        self.result = None
        if self.player1.player_choice == self.player2.player_choice:
            self.result = 'draw'
        elif self.player1.player_choice == 'rock' and self.player2.player_choice == 'scissors':
            self.result = 'You win'
            self.player1_score +=1
        elif self.player1.player_choice == 'rock' and self.player2.player_choice == 'paper':
            self.result = 'Computer wins'
            self.player2_score += 1
        elif self.player1.player_choice == 'paper' and self.player2.player_choice == 'rock':
            self.result = 'You win'
            self.player1_score +=1
        elif self.player1.player_choice == 'paper' and self.player2.player_choice == 'scissors':
            self.result = 'Computer wins'
            self.player2_score += 1
        elif self.player1.player_choice == 'scissors' and self.player2.player_choice == 'rock':
            self.result = 'Computer wins'
            self.player2_score += 1
        elif self.player1.player_choice == 'scissors' and self.player2.player_choice == 'paper':
            self.result = 'You win'
            self.player1_score +=1

        


def get_computer_choice():
    computer_choice = 0
    x = random.randint(1,3)

    if x == 1:
        computer_choice = 'rock'
    elif x == 2:
        computer_choice = 'scissors'
    elif x == 3:
        computer_choice = 'paper'

    return computer_choice

