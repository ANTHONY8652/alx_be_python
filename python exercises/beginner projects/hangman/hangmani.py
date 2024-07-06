import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    print("Welcome to Hangman!")
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 80  # Set the maximum number of incorrect guesses allowed

    while len(word_letters) > 0 and lives > 0:
        # Show the current state of the word
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print("Current word: ", ' '.join(word_list))

        # Show the letters the user has guessed
        print("Used letters: ", ' '.join(used_letters))

        # Get user input
        user_letter = input('Guess a letter: ').upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                print(f"Sorry, {user_letter} is not in the word.")
                lives -= 1
        elif user_letter in used_letters:
            print(f"You have already guessed {user_letter}. Please try again.")
        else:
            print("Invalid character. Please try again.")

    # Game over
    if lives == 0:
        print(f"Sorry, you lost! The word was {word}.")
    else:
        print(f"Congratulations! You guessed the correct word {word}!")

hangman()
