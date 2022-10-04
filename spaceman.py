import random
import re
from time import sleep
from os import system

def load_word():

    '''
    A function that reads a text file of words and randomly selects one to use as the secret word from the list.
    
    Input - none

    Return - string: secret word from the document to be used in the spaceman game
    '''

    file = open('./words.txt', 'r')
    words_list = file.readlines()
    file.close()
    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):

    '''
    A function that checks if all the letters of the secret word have been guessed.

    Input - secret_word (string): the secret word that the player is trying to guess
            letters_guessed (list of strings): list of letters that have been guessed so far
    
    Return - (bool): true only if all the letters in secret_word are in letters_guessed, otherwise false
    '''

    total_guessed_letters = 0
    for letter in secret_word:
        if letter in letters_guessed:
            total_guessed_letters += 1
    if total_guessed_letters == len(secret_word):
        return True
    else:
        return False

def get_guessed_word(secret_word, letters_guessed, guess):

    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.

    Input - secret_word (string): described above
            letters_guessed (list of strings): described above
            guess (string): single character to be compared against the characters of the secret word

    Return - letters_guessed (list of strings): list of guessed characters and underscores representing the guessed/unguessed characters as the player works towards revealing the secret word
    '''

    for character in range(len(secret_word)):
        if secret_word[character] == guess:
            letters_guessed[character] = guess
    return letters_guessed

def is_guess_in_word(guess, secret_word):

    '''
    A function to check if the guessed letter is in the secret word

    Inputs - guess (string): described above
             secret_word (string): described above

    Return - is_in_word (bool): True if guess is in secret_word, otherwise False
    '''

    character = 0
    is_in_word = False
    for character in secret_word:
        if character == guess:
            is_in_word = True
            return is_in_word

def get_guess(letters_guessed, remaining_letters):

    '''
    A function to prompt the user for their single character guess input with error correcting for invalid inputs
    or previously guessed letters

    Input - letters_guessed (list of strings): described above
            remaining_letters (list of strings): remaining letters from the alphabet that have not yet been guessed
    
    Return - guess.lower() (string): validated and case-corrected string character as the player's guess
    '''

    guess_check = False
    guess = input(("Please enter a single letter as your guess > "))
    while guess_check == False:
        if len(guess) != 1 or not re.match("^[a-zA-Z]+$", guess):
            guess = input("That was not a valid alphabetic character or you entered more than one character.  Please enter a new guess > ")
        elif guess.lower() not in remaining_letters:
            guess = input(f"You've already guessed the letter [ {guess} ].  Please enter a new guess > ")
        else:
            guess_check = True
    return guess.lower()

def compress_string(letters_guessed):

    '''
    A function to convert array of letters_guessed to a string for output aesthetics

    Input - letters_guessed (list of strings): described above

    Return - compressed_string (string): letters_guessed as a string instead of a list for aesthetics
    '''

    compressed_string = ''
    for letter in letters_guessed:
        compressed_string += letter
    return compressed_string

def difficulty():

    '''
    A function to get a difficulty setting from the player and set the corresponding max_incorrect_guesses value

    Input - none

    Return - max_incorrect_guesses (int)
    '''

    difficulty_check = False
    max_incorrect_guesses = 7
    print("""
Please choose a difficulty level (1 - 4):
1 - \33[32mEasy\33[0m - 7 incorrect guesses maximum
2 - \033[36mNormal\33[0m - 5 incorrect guesses maximum
3 - \33[33mHard\33[0m - 4 incorrect guesses maximum
4 - \33[31mNIGHTMARE\33[0m - 3 incorrect guesses maximum
""")
    while difficulty_check == False:
        difficulty = input("Enter your difficulty choice > ")
        match difficulty:
            case '1':
                max_incorrect_guesses = 7
                difficulty_check = True
                print("You have chosen: \33[32mEasy\33[0m - 7 maximum incorrect guesses")
                break
            case '2':
                max_incorrect_guesses = 5
                difficulty_check = True
                print("You have chosen: \033[36mNormal\33[0m - 5 maximum incorrect guesses")
                break
            case '3':
                max_incorrect_guesses = 4
                difficulty_check = True
                print("You have chosen: \33[33mHard\33[0m - 4 maximum incorrect guesses")
                break
            case '4':
                max_incorrect_guesses = 3
                difficulty_check = True
                print("You have chosen: \33[31mNIGHTMARE\33[0m - 3 maximum incorrect guesses")
                break
    print()       
    return max_incorrect_guesses

def score_change(max_incorrect_guesses, total_score, secret_word, letters_guessed):

    '''
    A function that uses is_word_guessed and  handle scoring across multiple difficulties

    Input - max_incorrect_guesses (int): see above
            secret_word (string): see above
            letters_guessed (list of strings): see above
            total_score (dict): Takes initialized dictionary that keeps track of wins and losses for each difficulty

    Return - total_score (dict): Returns dict containing updated scores
    '''

    match max_incorrect_guesses:
        case 7:
            if is_word_guessed(secret_word, letters_guessed) == True:
                total_score['easy_w'] += 1
            else: total_score['easy_l'] += 1
        case 5:
            if is_word_guessed(secret_word, letters_guessed) == True:
                total_score['normal_w'] += 1
            else: total_score['normal_l'] += 1            
        case 4:
            if is_word_guessed(secret_word, letters_guessed) == True:
                total_score['hard_w'] += 1
            else: total_score['hard_l'] += 1            
        case 3:
            if is_word_guessed(secret_word, letters_guessed) == True:
                total_score['nightmare_w'] += 1
            else: total_score['nightmare_l'] += 1
    return total_score

def scoreboard(total_score):

    '''
    A function that uses the updated total_scoreboard to print out the final scores for each difficulty at the end of the game

    Input - total_score (dict): see above

    Return - none
    '''


    print()
    print("Thanks for playing!")
    print()
    print("Your final score for this session was:")
    if total_score['easy_w'] != 0 or total_score['easy_l'] != 0:
        print(f"\33[32mEasy\33[0m difficulty - \33[32m{total_score['easy_w']} wins\33[32m, \33[31m{total_score['easy_l']} losses")
    if total_score['normal_w'] != 0 or total_score['normal_l'] != 0:
        print(f"\033[36mNormal\33[0m difficulty - \33[32m{total_score['normal_w']} wins\33[32m, \33[31m{total_score['normal_l']} losses")
    if total_score['hard_w'] != 0 or total_score['hard_l'] != 0:
        print(f"\33[33mHard\33[0m difficulty - \33[32m{total_score['hard_w']} wins\33[32m, \33[31m{total_score['hard_l']} losses")
    if total_score['nightmare_w'] != 0 or total_score['nightmare_l'] != 0:
        print(f"\33[31mNIGHTMARE\33[0m difficulty: - \33[32m{total_score['nightmare_w']} wins\33[32m, \33[31m{total_score['nightmare_l']} losses")

def spaceman(secret_word, total_score):

    '''
    A function that handles the calls of the main functions for the game of Spaceman.

    Input - secret_word (string): see above
            total_score (dict): see above

    Return - total_score
    '''

# A function that controls the game of spaceman. Will start spaceman in the command line.

    # initializing variables
    incorrect_guesses = 0
    max_incorrect_guesses = 7
    guess = ''
    letters_guessed = []
    remaining_letters = []

    #this was faster than typing the alphabet as an array that I can .pop from
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for letter in alphabet:
        remaining_letters.append(letter)

    for character in secret_word:
        letters_guessed.append('_')

    max_incorrect_guesses = difficulty()
    print(f"The secret word is {len(secret_word)} characters long.")
    print
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
            sleep(2)
            system('clear')
            if is_word_guessed(secret_word, letters_guessed) == True:
                print(f"\33[32mYou've guessed the secret word!\33[0m The secret word was '\33[32m{secret_word}\33[0m'!")
                print()
                score_change(max_incorrect_guesses, total_score, secret_word, letters_guessed)
                break
        else:
            incorrect_guesses += 1
            if incorrect_guesses == max_incorrect_guesses:
                print(f"Sorry, you've made \33[31m{max_incorrect_guesses} incorrect guesses and the game is over\33[0m.  The secret word was '\33[31m{secret_word}\33[0m'")
                print()
                score_change(max_incorrect_guesses, total_score, secret_word, letters_guessed)
            else:
                print(f"Your guess [ {guess} ] was \33[31mnot correct\33[0m!  You have {max_incorrect_guesses - incorrect_guesses} incorrect guesses remaining.")
                sleep(2)
                system('clear')
    return total_score

# test pen-----------------------------------

def test():
    letters_guessed = ''
    secret_word = load_word()
    print(secret_word)
    spaceman(secret_word)
    
# test()

#-------------------------------------------

# Program execution starts here

sleep(1.5)
system('clear')

# Preamble text with rules

print("""Welcome to my Spaceman game!

Rules:

The system will choose a random secret word from a dictionary. The player will select a letter to guess from the secret word until the whole word has been revealed, or the player has reached their maximum incorrect guesses.

Good luck!""")

# Total_score holds an array of scores for each difficulty

play_again = True
total_score = {
    'easy_w': 0,
    'easy_l': 0,
    'normal_w': 0,
    'normal_l': 0,
    'hard_w': 0,
    'hard_l': 0,
    'nightmare_w': 0,
    'nightmare_l': 0,
}

# These function calls that will start and loop the game until the player is done

while play_again == True:
    letters_guessed = ''
    secret_word = load_word()
    spaceman(secret_word, total_score)
    play_again_prompt = input("Would you like to play again? Enter y / n > ")
    while play_again_prompt.lower() != 'y' and play_again_prompt.lower() != 'n':
        play_again_prompt = input("Invalid input. Would you like to play again? Enter y / n > ")
    if play_again_prompt == 'y':
        play_again = True
    else:
        play_again = False
scoreboard(total_score)
print()





