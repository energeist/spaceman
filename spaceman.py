import random
import re

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('./words.txt', 'r')
    words_list = f.readlines()
    f.close()
    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
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
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet

    # pass
    for character in range(len(secret_word)):
        if secret_word[character] == guess:
            letters_guessed[character] = guess
    return letters_guessed



def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''
    #TODO: check if the letter guess is in the secret word

    # pass
    #print(f"Debug - in is_guess_in_word function - guessed letter: {guess}")
    print(f"Debug in IGIW function- value of guess received in is_guess_in_word function: [ {guess} ]")
    print(f"Debug - secret word: {secret_word}")
    character = 0
    is_in_word = False
    for character in range(len(secret_word)):
        print(f"index: {character}, secret_word character at index: {secret_word[character]}")
        if secret_word[character] == guess:
            is_in_word = True
            return is_in_word

def get_guess(letters_guessed):
    guess_check = False
    guess = input("Please enter a single letter as your guess > ")
    while guess_check == False:
        if len(guess) != 1 or not re.match("^[a-zA-z]+$", guess):
            guess = input("That was not a valid alphabetic character or you entered more than one character.  Please enter a new guess > ")
        elif guess in letters_guessed:
            guess = input("You've already guessed that letter.  Please enter a new guess > ")
        else:
            guess_check = True
    #print(f"Debug - in get_guess function - guessed letter: {guess}")
    return guess        

def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''
    # initializing variables
    incorrect_guesses = 0
    # set incorrect guesses to 7 to start, will add in difficulty selection to make this dynamic
    max_incorrect_guesses = 7
    guess = ''
    letters_guessed = []
    for letter in range((len(secret_word))):
        letters_guessed.append('_')

    while incorrect_guesses < max_incorrect_guesses:
        print (f'Letters guessed: {letters_guessed}')
        guess = get_guess(letters_guessed)
        #print(f"Debug - spaceman body function - guessed letter: {guess}")
        get_guessed_word(secret_word, letters_guessed, guess)
        print(f"Debug - returned from function is_guess_in_word: {is_guess_in_word(guess, secret_word)}")
        if is_guess_in_word(guess, secret_word) == True:
            print(f"Your guess [ {guess} ] was correct!")
        else:
            incorrect_guesses += 1
            print(f"Your guess [ {guess} ] was not correct!  You have {max_incorrect_guesses - incorrect_guesses} incorrect remaining.")
        if is_word_guessed(secret_word, letters_guessed) == True:
            print(f"You've guessed the word!  It was {secret_word}!")
            break
    if incorrect_guesses == max_incorrect_guesses:
        print(f"Sorry, you've made {max_incorrect_guesses} incorrect guesses and the game is over.  The secret word was {secret_word}")
            

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


test()

#-------------------------------------------
#These function calls that will start the game

# get_guess(letters_guessed)

#     print("""
# Welcome to my Spaceman game!

# Rules:

# The system will choose a random word from a dictionary.  The player will select a letter to guess from the secret word until the whole word has been revealed, or the player has 7 incorrect guesses.

# Good luck!
#     """)

