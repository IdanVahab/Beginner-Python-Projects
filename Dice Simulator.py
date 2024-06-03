import random


def roll_dice(amount: int = 2) -> list[int]:
    if amount <= 0:
        raise ValueError

    rolls: list[int] = []
    for i in range(amount):
        random_roll: int = random.randint(1, 6)
        rolls.append(random_roll)

    return rolls
def main():
    while True:
        user_input: str = input('How many dice would you like to roll? (type "exit" to quit): ')
        if user_input.lower() == 'exit':
            print('Thanks for playing!')
            break

        try:
            amount = int(user_input)
            results = roll_dice(amount)
            print(f'You rolled: {results}')
        except ValueError:
            print('Please enter a valid number.')

if __name__ == '__main__':
   main()