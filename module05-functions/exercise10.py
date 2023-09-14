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


def create_secret(level):
    return 123

def play(guess):
    return 123

# global variables
game_level = 3
secret = create_secret(game_level)
max_moves = 10
lives = 3

while game_level <= 10:
    guess = int(input("Guess: "))
    play(guess)