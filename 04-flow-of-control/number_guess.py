import random

number_to_guess = random.randint(1, 10)

guess = int(input('Please enter your guess: '))
if guess == number_to_guess:
    print(f'Well done you guess the number {number_to_guess}')
else:
    print(f'Sorry your guess was wrong, the number was {number_to_guess}')
