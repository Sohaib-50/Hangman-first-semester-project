import random
from time import sleep


def get_word():
    '''function to randomly choose and return a word from the file words.txt'''
    with open("words.txt", "r") as wordsfile:
        return random.choice(wordsfile.read().split())


def print_initial_messages(WORD):
    '''function to print the initital welcoming messages and instructions.
    Takes input the parameter WORD so that it can print its length.'''

    print("-" *60)
    print(f"{'Welcome to the Hangman game!':~^60s}") #padded heading
    print("-" *60)
    print(f"I am thinking of a word that is {len(WORD)} characters long.")
    print("You have to guess my word by guessing one character at a time.")
    print()
    
    print("""You have total 6 guesses and 3 warnings. For every wrong
alphabetical character you guess, you'll loose a guess (2 guesses lost if
you guess a wrong vowel!)""")
    print()
    
    print("""If you enter a character that is already guessed or something
invalid like a special character or a word with more than 1 characters,
you'll be warned. After 3 warnings, you'll start loosing guesses.""")


def display_countdown(n):
    '''function to display count down starting from n down to 1 with
    slight gap between each number display.
    Parameter n must be a positive integer.'''
    while n>1:
        print(n)
        sleep(0.5)
        return display_countdown(n-1)
    print(n)
    return 


def is_vowel(c):
    '''function to check if the parameter input (c) is a vowel or not.
    Parameter should be a character.'''
    if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
        return True
    else:
        return False


def give_warning(guesses, warnings):
    '''function to warn the user and either decrease warnings or guesses.
    Takes input as parameters guesses and warnings so that it can change them.
    Returns both guesses and warnings.'''
    if warnings: #warnings remaining
        warnings -= 1
        print(f"You've been warned.\n")
    else:
        guesses -= 1
        print("You have no warnings left so you lose a guess.")
    return guesses, warnings


def adjust_out_word(guess, out_word, WORD):
    '''function to replace underscores in out_word by the character
    guessed on those indexes where the parameter "guess" is present in original WORD.'''
    for i in range(len(WORD)):
        if WORD[i] == guess:
            out_word[i] = guess
    return out_word
    

def  count_unique_chars(s):
    '''function to count and return number of unique characters
    in the string parameter s'''
    unique_chars = []
    for ch in s:
        if s.count(ch) > 1:
            pass
        else:
            unique_chars.append(ch)
         
    return len(unique_chars)
