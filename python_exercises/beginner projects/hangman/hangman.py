import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words) #randomly chooses something\n from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word

def hangman():
    print("Welcome to Hangman!")
    word = get_valid_word(words)
    word_letters = set(word) #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what the user has guessed

    #guessing user input
    user_letter = input('Guess a letter: ').upper()
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)

    elif user_letter in used_letters:
        print("You have already guessed that character idiot. Please try again")
    else:
        print("Invalid character chump. Try again")

user_input = input('What is your word?:')
