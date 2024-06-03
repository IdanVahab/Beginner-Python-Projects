import random
import sys


class RPS:
    def __init__(self):
        """
        Initializes the Rock Paper Scissors game.
        """
        print('Welcome to Rock Paper Scissors!')

        self.moves: dict = {'rock': 'r', 'paper': 'p', 'scissors': 's'}
        self.valid_moves = ['rock', 'paper', 'scissors']
        self.user_wins: int = 0  # Counter for user's wins
        self.ai_wins: int = 0  # Counter for AI's wins
        self.total_games: int = 0  # Counter for total games played

    def play_game(self):
        """
        Plays a round of the game.
        Prompts the user for input and compares it with AI's move.
        """
        while self.user_wins < 3 and self.ai_wins < 3:
            user_move: str = input('Rock, paper, or scissors: ')

            if user_move == 'exit':
                print(f'Thanks for playing! You won {self.user_wins} times.')
                sys.exit()

            if user_move not in self.valid_moves:
                print('Invalid move!')
                continue

            ai_move: str = random.choice(self.valid_moves)

            self.display_moves(user_move, ai_move)
            self.check_move(user_move, ai_move)
            self.total_games += 1

            print(f'Total games played: {self.total_games}')

        if self.user_wins == 3:
            print('Congratulations! You won best of 5 games and won the match!')
        else:
            print('AI wins the match! Better luck next time!')

    def display_moves(self, user_move: str, ai_move: str):
        """
        Displays the moves of both the user and the AI.

        Args:
            user_move (str): The user's move.
            ai_move (str): The AI's move.
        """
        print('----')
        print(f'You: {self.moves[user_move]}')
        print(f'AI: {self.moves[ai_move]}')
        print('----')

    def check_move(self, user_move: str, ai_move: str):
        """
        Checks the moves and determines the winner.

        Args:
            user_move (str): The user's move.
            ai_move (str): The AI's move.
        """
        if user_move == ai_move:
            print('It\'s a tie!')
        elif (user_move == 'rock' and ai_move == 'scissors') or \
                (user_move == 'paper' and ai_move == 'rock') or \
                (user_move == 'scissors' and ai_move == 'paper'):
            self.user_wins += 1  # Increment user's win counter
            wins_needed = 5 - self.user_wins
            print(f'You win! You have won {self.user_wins} times. You need {wins_needed} more wins to win the match.')
        else:
            self.ai_wins += 1  # Increment AI's win counter
            wins_needed = 5 - self.user_wins
            print(f'You lose! You need {wins_needed} more wins to win the match.')


if __name__ == '__main__':
    rps = RPS()
    rps.play_game()
