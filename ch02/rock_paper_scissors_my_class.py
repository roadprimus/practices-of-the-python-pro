# My implementation of the game with class.
import random


class Game:
    ROCK = 'rock'
    PAPER = 'paper'
    SCISSORS = 'scissors'

    OPTIONS = [ROCK, PAPER, SCISSORS]

    DRAW = 'draw'
    HUMAN = 'human'
    COMPUTER = 'computer'
    RESULT = [DRAW, HUMAN, COMPUTER]

    def __init__(self):
        self.human_choice = None
        self.computer_choice = None
        self.winner = None
    
    def start(self):
        self.print_choice_message()
        self.do_human_choice()
        self.do_computer_choice()
        self.determine_winner()
        self.print_result()

    def print_choice_message(self):
        """Prints choice message for the human."""
        
        options_with_numbers = [
            f'({num}) {opt}'for num, opt in enumerate(self.OPTIONS, start=1)
        ]
        print('\n'.join(options_with_numbers))

    def do_human_choice(self):
        """Gets and prints the human choice.

        Returns:
            str: The human's choice.

        """
        self.human_choice = self.OPTIONS[
            int(input('Enter the number of your choice: ')) - 1
        ]
        print(f'You chose {self.human_choice}')

    def do_computer_choice(self):
        """Gets and prints the computer choice.

        Returns:
            str: The computers's choice.

        """
        self.computer_choice = random.choice(self.OPTIONS)
        print(f'The computer chose {self.computer_choice}')

    def determine_winner(self):
        """Determines the winner of the game or a draw.

        Returns:
            str: The winnre of the game or a draw.

        """
        winner = self.DRAW
        if self.human_choice != self.computer_choice:
            if self.human_choice == self.ROCK:
                winner = self.COMPUTER if self.computer_choice == self.PAPER else self.HUMAN
            elif self.human_choice == self.PAPER:
                winner = self.COMPUTER if self.computer_choice == self.SCISSORS else self.HUMAN
            else:
                winner = self.COMPUTER if self.computer_choice == self.ROCK else self.HUMAN

        self.winner = winner


    def print_result(self):
        """Prints the result of the game."""

        result = 'Draw!'
        if self.winner != self.DRAW:
            if self.winner == self.HUMAN:
                result = f'Yes, {self.human_choice} beat {self.computer_choice}!'
            else:
                result = f'Sorry, {self.computer_choice} beat {self.human_choice}'
        
        print(result)


if __name__ == '__main__':
    game = Game()
    game.start()
