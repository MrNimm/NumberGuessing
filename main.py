import random

max_attempt = 8


#Set Rules
def display_rules():
    print("Welcome to the game (You just lost it by the way)!\n")
    print("There is a chosen number betwixt 1 and 100.")
    print(f"You have {max_attempt} attempts to chose the correct number.\n")

#The Game
def play_game(number, attempt):
    if attempt > max_attempt:
        print("\nGame Over man, Game over")
        print("Correct number: ", number)
        return

    guess = input(f"Attempt {attempt}/{max_attempt} - Enter your guess: ")

    try:
        guess = int(guess)
    except ValueError:
        print("Please enter a valid number.\n")
        return play_game(number, attempt)

    if guess < 1 or guess > 100:
        print("please enter a number betwixt 1 and 100. \n")
        return play_game(number, attempt)

    check_guess = lambda x, y: "correct" if x == y else (
        "low" if x < y else "high"
    )

    result = check_guess(guess, number)

    if result == "correct":
        print("\nCongratulations! You have the correct number.\n")
        print(f"You guessed it in {attempt} attempt(s).")
        return

    if result == "low":
        print("Too low!\n")
    else:
        print("Too high!\n")

    play_game(number, attempt + 1)

#Start Game
display_rules()

random_number = random.randint(1, 100)

play_game(random_number, 1)

