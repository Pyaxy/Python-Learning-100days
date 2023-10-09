import random
from guessing_game_art import guessing_game_art


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# begin information and let user chose a difficulty
def welcome():
    print(guessing_game_art)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard'").lower()
    if difficulty == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
    
# main func
def start():
    attempts = welcome()
    number = random.randint(1,100)
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess:"))
        if guess > number:
            print("Too high")
            print("Guess again")
        elif guess < number:
            print("Too low")
            print("Guess again")
        else:
            print("Congratulations! You guess the number!")
            return
    
    print(f"You have {attempts} attempts remaining to guess the number.")
    print("You lose!")
    
start()