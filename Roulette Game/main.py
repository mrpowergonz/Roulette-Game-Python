import random

# List of words for the game
words = ["PYTHON", "PROGRAMMING", "WHEEL", "FORTUNE", "PUZZLE", "GUESS"]

def select_random_word():
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display

def get_guess(guessed_letters):
    while True:
        guess = input("Guess a letter: ").upper()
        if len(guess) == 1 and guess.isalpha() and guess not in guessed_letters:
            return guess
        else:
            print("Please enter a single letter that you haven't guessed before.")

def wheel_of_fortune():
    print("Welcome to Wheel of Fortune!")

    while True:
        word_to_guess = select_random_word()
        guessed_letters = []
        attempts = 7  # Set the number of attempts

        while attempts > 0:
            print("\n" + display_word(word_to_guess, guessed_letters))
            print(f"Attempts left: {attempts}")
            
            guess = get_guess(guessed_letters)
            guessed_letters.append(guess)

            if guess in word_to_guess:
                print("Good guess!")
                if all(letter in guessed_letters for letter in word_to_guess):
                    print(f"Congratulations! You guessed the word: {word_to_guess}!")
                    break
            else:
                print("Incorrect guess.")
                attempts -= 1

        if attempts == 0:
            print(f"Sorry, you ran out of attempts. The word was: {word_to_guess}")

        play_again = input("Press Enter to play again or 'q' to quit: ")
        if play_again.lower() == "q":
            break

# Run the game
wheel_of_fortune()
