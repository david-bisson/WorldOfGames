def welcome(name):
    welcome_message = f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play."
    return welcome_message


def load_game():
    print("Please choose a game to play:")
    print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
    print("2. Guess Game - guess a number and see if you chose like the computer")
    print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS")

    # Getting the game choice from the user
    game_choice = int(input("Enter the number of the game you choose (1-3): "))

    # Validating the game choice
    while game_choice not in [1, 2, 3]:
        game_choice = int(input("Invalid input. Please enter a number between 1 and 3: "))

    # Getting the level of difficulty from the user
    difficulty_level = int(input("Please choose game difficulty from 1 to 5: "))

    # Validating the difficulty level
    while difficulty_level not in [1, 2, 3, 4, 5]:
        difficulty_level = int(input("Invalid input. Please enter a number between 1 and 5: "))

    return f"You have chosen game {game_choice} with difficulty level {difficulty_level}."


# Test the functions
name = input("Enter your name: ")
print(welcome(name))
print(load_game())
