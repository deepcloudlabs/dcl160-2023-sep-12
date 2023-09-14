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

# global variables
game_level = 3
secret = create_secret(game_level)
max_moves = 10
lives = 3
moves = 0


def evaluate_move(guess, secret):
    pass


while game_level <= 10:
    guess = int(input("Guess: "))
    moves = moves + 1
    if guess == secret:
        print(f"You win the level {game_level}.")
        game_level = game_level + 1
        secret = create_secret(game_level)
        moves = 0
    elif moves > max_moves:
        print(f"You lose the level {game_level}.")
        lives = lives - 1
        if lives == 0:
            print(f"You lose the game.")
            break
        secret = create_secret(game_level)
        moves = 0
    else:
        message = evaluate_move(guess,secret)
        print(f"Guess: {guess}, Message: {message}")