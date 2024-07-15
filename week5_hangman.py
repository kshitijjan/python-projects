import random

# Word categories
categories = {
    "Animals": ["elephant", "giraffe", "dolphin"],
    "Countries": ["brazil", "canada", "germany"],
    "Movies": ["inception", "gladiator", "avatar"]
}

# Hangman stages
hangman_stages = [
    """
     -----
     |   |
         |
         |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    --------
    """
]

def choose_category():
    print("Choose a category: Animals, Countries, Movies")
    while True:
        category = input().capitalize()
        if category in categories:
            return random.choice(categories[category])
        else:
            print("Invalid category. Please choose again.")

def set_difficulty():
    print("Select difficulty: Easy, Medium, Hard")
    while True:
        difficulty = input().capitalize()
        if difficulty == "Easy":
            return 10, 5  # 10 guesses, minimum word length 5
        elif difficulty == "Medium":
            return 7, 7
        elif difficulty == "Hard":
            return 5, 9
        else:
            print("Invalid difficulty. Please choose again.")

def display_hangman(stage):
    print(hangman_stages[stage])

def use_hint(word, guessed_letters):
    for letter in word:
        if letter not in guessed_letters:
            print(f"Hint: The word contains the letter '{letter}'")
            return letter

def play_game():
    word = choose_category()
    max_incorrect_guesses, min_word_length = set_difficulty()
    
    guessed_letters = set()
    correct_letters = set(word)
    incorrect_guesses = 0
    hint_used = False

    print("Welcome to Hangman!")

    while incorrect_guesses < max_incorrect_guesses:
        display_hangman(incorrect_guesses)
        print("Guessed letters: ", " ".join(sorted(guessed_letters)))
        
        word_display = [letter if letter in guessed_letters else "_" for letter in word]
        print("Word: ", " ".join(word_display))

        if set(word_display) == correct_letters:
            print("Congratulations! You've guessed the word!")
            break

        guess = input("Guess a letter or type 'hint' for a hint: ").lower()

        if guess == "hint":
            if not hint_used:
                hint_letter = use_hint(word, guessed_letters)
                guessed_letters.add(hint_letter)
                hint_used = True
            else:
                print("Hint already used!")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
        elif guess in word:
            guessed_letters.add(guess)
        else:
            guessed_letters.add(guess)
            incorrect_guesses += 1

    if incorrect_guesses == max_incorrect_guesses:
        display_hangman(incorrect_guesses)
        print(f"Game over! The word was '{word}'.")

def multiplayer_mode():
    print("Multiplayer mode: Player 1 and Player 2 take turns to guess.")
    word = choose_category()
    max_incorrect_guesses, min_word_length = set_difficulty()

    guessed_letters = set()
    correct_letters = set(word)
    incorrect_guesses = 0
    current_player = 1

    print("Welcome to Multiplayer Hangman!")

    while incorrect_guesses < max_incorrect_guesses:
        display_hangman(incorrect_guesses)
        print("Guessed letters: ", " ".join(sorted(guessed_letters)))
        
        word_display = [letter if letter in guessed_letters else "_" for letter in word]
        print("Word: ", " ".join(word_display))

        if set(word_display) == correct_letters:
            print(f"Player {current_player} wins! You've guessed the word!")
            break

        guess = input(f"Player {current_player}, guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter.")
        elif guess in word:
            guessed_letters.add(guess)
        else:
            guessed_letters.add(guess)
            incorrect_guesses += 1

        current_player = 2 if current_player == 1 else 1

    if incorrect_guesses == max_incorrect_guesses:
        display_hangman(incorrect_guesses)
        print(f"Game over! The word was '{word}'.")

def main():
    print("Welcome to Enhanced Hangman!")
    print("1. Single Player")
    print("2. Multiplayer")
    choice = input("Choose mode (1 or 2): ")

    if choice == "1":
        play_game()
    elif choice == "2":
        multiplayer_mode()
    else:
        print("Invalid choice. Exiting the game.")

if __name__ == "__main__":
    main()
