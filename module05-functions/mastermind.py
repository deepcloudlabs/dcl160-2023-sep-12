"""
Mastermind
Level: 3
Secret: 549
Lives: 3
Guess -> 123 -> "No match"
         456 -> -2
         574 -> -1+1
Max # of moves: 10 -> +1
Level -> 4 -> Secret: 3615
Level -> 10 -> Wins
"""
from random import randint


def create_random_digit(m=0, n=9):
    return randint(m, n)


def create_secret(level):
    digits = [create_random_digit(m=1)]
    while len(digits) < level:
        digit = create_random_digit()
        if digit not in digits:
            digits.append(digit)
    return int("".join([str(digit) for digit in digits]))

def play(guess):
    return 123

# global variables
game_level = 3
secret = create_secret(game_level)
max_moves = 10
lives = 3

"""
while game_level <= 10:
    guess = int(input("Guess: "))
    play(guess)
"""
print(create_secret(3))
