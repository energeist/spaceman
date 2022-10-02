import random
import re
from time import sleep
from os import system

def load_word():

    # A function that reads a text file of words and randomly selects one to use as the secret word from the list.
    # Returns: 
    #   string: The secret word to be used in the spaceman guessing game

    f = open('./words.txt', 'r')
    words_list = f.readlines()
    f.close()
    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):

    # A function that checks if all the letters of the secret word have been guessed.
    # Args:
    #     secret_word (string): the random word the user is trying to guess.
    #     letters_guessed (list of strings): list of letters that have been guessed so far.
    # Returns: 
    #     bool: True only if all the letters of secret_word are in letters_guessed, False otherwise

    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    # pass
    total_guessed_letters = 0
    for letter in range(len(secret_word)):
        if secret_word[letter] in letters_guessed:
            total_guessed_letters += 1
    if total_guessed_letters == len(secret_word):
        return True
    else:
        return False

def get_guessed_word(secret_word, letters_guessed, guess):

    # A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    # Args: 
    #     secret_word (string): the random word the user is trying to guess.
    #     letters_guessed (list of strings): list of letters that have been guessed so far.
    # Returns: 
    #     string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.


    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet

    for character in range(len(secret_word)):
        if secret_word[character] == guess:
            letters_guessed[character] = guess
    return letters_guessed



def is_guess_in_word(guess, secret_word):

    # A function to check if the guessed letter is in the secret word
    # Args:
    #     guess (string): The letter the player guessed this round
    #     secret_word (string): The secret word
    # Returns:
    #     bool: True if the guess is in the secret_word, False otherwise

    #TODO: check if the letter guess is in the secret word

    character = 0
    is_in_word = False
    for character in secret_word:
        if character == guess:
            is_in_word = True
            return is_in_word

def get_guess(letters_guessed, remaining_letters):
    guess_check = False
    # sleep(3)
    # system('clear')
    guess = input(("Please enter a single letter as your guess > "))
    while guess_check == False:
        if len(guess) != 1 or not re.match("^[a-zA-z]+$", guess):
            # sleep(1)
            # system('clear')
            guess = input("That was not a valid alphabetic character or you entered more than one character.  Please enter a new guess > ")
        elif guess.lower() not in remaining_letters:
            # sleep(1)
            # system('clear')
            guess = input(f"You've already guessed the letter [ {guess} ].  Please enter a new guess > ")
        else:
            guess_check = True
    return guess.lower()

# function to convert array of letters_guessed to a string for output aesthetics

def compress_string(letters_guessed):
    compressed_string = ''
    for letter in letters_guessed:
        compressed_string += letter
    return compressed_string

def spaceman(secret_word, total_score):

    # A function that controls the game of spaceman. Will start spaceman in the command line.
    # Args:
    #   secret_word (string): the secret word to guess.


    # initializing variables
    incorrect_guesses = 0
    # set incorrect guesses to 7 to start, will add in difficulty selection to make this dynamic
    max_incorrect_guesses = 7
    guess = ''
    letters_guessed = []
    remaining_letters = []

    #total score index 0 = wins, index 1 = losses
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for letter in alphabet:
        remaining_letters.append(letter)

    for character in secret_word:
        letters_guessed.append('_')

    print(f"The secret word is {len(secret_word)} characters long.")

    while incorrect_guesses < max_incorrect_guesses:
        print(f"Letters guessed in the secret word: {compress_string(letters_guessed)}")
        print(f'Unguessed letters: {" ".join(remaining_letters)}')
        print()
        guess = get_guess(letters_guessed, remaining_letters)
        if guess.lower() in remaining_letters:
            remaining_letters.pop(remaining_letters.index(guess.lower()))
        get_guessed_word(secret_word, letters_guessed, guess)
        if is_guess_in_word(guess, secret_word) == True:
            print(f"Your guess [ {guess} ] was \33[32mcorrect\33[0m!")
            if is_word_guessed(secret_word, letters_guessed) == True:
                print(f"\33[32mYou've guessed the secret word!\33[0m  It was '{secret_word}'!")
                total_score[0] += 1
                break
        else:
            incorrect_guesses += 1
            if incorrect_guesses == max_incorrect_guesses:
                print(f"Sorry, you've made \33[31m{max_incorrect_guesses} incorrect guesses\33[0m! and the game is over.  The secret word was '{secret_word}'")
                print()
                total_score[1] += 1
            else:
                print(f"Your guess [ {guess} ] was \33[31mnot correct\33[0m!  You have {max_incorrect_guesses - incorrect_guesses} incorrect remaining.")
    return total_score


            

    #TODO: show the player information about the game according to the project spec

    #TODO: Ask the player to guess one letter per round and check that it is only one letter

    #TODO: Check if the guessed letter is in the secret or not and give the player feedback

    #TODO: show the guessed word so far

    #TODO: check if the game has been won or lost






# test pen-----------------------------------

def test():
    letters_guessed = ''
    secret_word = load_word()
    print(secret_word)
    spaceman(secret_word)
    
# test()

#-------------------------------------------

# Preamble text with rules

print("""
Welcome to my Spaceman game!

Rules:

The system will choose a random secret word from a dictionary. The player will select a letter to guess from the secret word until the whole word has been revealed, or the player has 7 incorrect guesses.

Good luck!
""")

# These function calls that will start and loop the game until the player is done

play_again = True
total_score = [0, 0]

while play_again == True:
    letters_guessed = ''
    secret_word = load_word()
    spaceman(secret_word, total_score)
    play_again_prompt = input("Would you like to play again? Enter y / n > ")
    while play_again_prompt.lower() != 'y' and play_again_prompt.lower() != 'n':
        play_again_prompt = input("Invalid input. Would you likke to play again? Enter y / n > ")
    if play_again_prompt == 'y':
        play_again = True
    else:
        play_again = False
    sleep(1.5)
    system('clear')
print(f"Thanks for playing! Your final score was \33[32m{total_score[0]} wins\33[0m and \33[31m{total_score[1]} losses\33[0m.")





