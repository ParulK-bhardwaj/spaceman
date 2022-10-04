# for isalpha
from ast import increment_lineno
from curses.ascii import isalpha
# to import random words from the file.
import random

# The following variables will allow us to get the incorrect guesses in one list and correct guesses in one list.
# And later display them in the game display as well.

correct_guesses = []
incorrect_guesses = []

# Setting this as a constant variable, learned it from pylint that a const variable should be all caps and words will be devided by "_".
# Also setting the allowed number of guesses will allow us to have the flexibility if we decided to offer more set guesses, once the game go live. 
# Also DRY.
GUESSES_ALLOWED = 7


def load_word():
    """
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.

    Returns:
           string: The secret word to be used in the spaceman guessing game
    """

    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, correct_guesses):
    """
    A function that checks if all the letters of the secret word have been guessed.

    Parameters:
        secret_word (string): the random word the user is trying to guess.
        correct_guesses (list of strings): list of letters that have been correctly guessed so far.

    Returns:
        bool: true only if all the letters of secret_word are in correct_guesses
    """
    # Looping through the letters in the secret_word to
    # check if a letter is in correct guesses and if the user has guessed all the letters of the secret_word.

    player_guess = ""
    guessed_the_word = False
    for i in range(secret_word_length):
        if secret_word [i] in correct_guesses:
            player_guess += secret_word[i]
            if player_guess == secret_word:
                guessed_the_word = True
    return guessed_the_word

def get_guessed_word(secret_word, correct_guesses):
    """
    This function is used to get a string showing the correct guesses so far in the secret word and
    underscores for letters that have not been guessed yet.

    Parameter:
        secret_word (string): the random word the user is trying to guess.
        correct_guesses (list of strings): list of letters that have been correctly guessed so far.

    Returns:
        string: letters and underscores.
        For correctly guessed letters in the word, the string should contain the letter at the correct position.
        For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    """

    # Looping through the letters in secret word and build a string that 
    # shows the letters that have been guessed correctly so far that are saved in correct guesses
    # and underscores for the letters that have not been guessed yet
    guessed_word_tillnow = ""

    for i in range(secret_word_length):
        if secret_word[i] in correct_guesses:
            guessed_word_tillnow += secret_word[i]
        else:
            guessed_word_tillnow += "_"
    return guessed_word_tillnow


def is_guess_in_word(guess_input, secret_word):
    '''
    A function to check if the guessed letter is in the secret word

    Parameters:
        guess_input (string): The letter the player guessed this round
        secret_word (string): The secret word

    Returns:
        list: append the guess_input into the correct and incorrect_guesses list

    '''
    #TODO: check if the letter guess is in the secret word

    if guess_input in secret_word:
        correct_guesses.append(guess_input)
    else:
        incorrect_guesses.append(guess_input)
        
def spaceman(secret_word):
    """
    A function that controls the game of spaceman. Will start spaceman in the command line.

    Args:
      secret_word (string): the secret word to guess.

    """
    #TODO: show the player information about the game according to the project spec
    print("\nWelcome to Spaceman!\n")
    
    print(f"The secret word contains: {secret_word_length} letters\n")
    
    #TODO: Ask the player to guess one letter per round and check that it is only one letter

    print(f"You have {GUESSES_ALLOWED} incorrect guesses, please enter one letter per round\n") 

    print("----------------------------------------------------------")

    game_on = True

    while game_on is True:
        while True:
            # converting input into lowercase to avoid case-sensitivity
            # imported isalpha to check if the input is a letter and is not a specialcharacter or a number or a blank
            
            guess_input = input("Enter a letter: ").lower()
            if len(guess_input) != 1 or isalpha(guess_input) is not True:
                print("You can only enter ONE LETTER per round, please enter one letter at a time")
            elif guess_input in correct_guesses or guess_input in incorrect_guesses:
                print("You have already gueesed this letter! please enter another letter.")
            else:
                break
        # call the function before so that the guess show up in correct or incorrect_guesses list 
        is_guess_in_word(guess_input, secret_word)
    
        #TODO: show the guessed word so far
        print(f"\nGuessed word so far: {get_guessed_word(secret_word, correct_guesses)}")

        #TODO: Check if the guessed letter is in the secret or not and give the player feedback
        print(f"\nHere is the list of the correct guesses: {correct_guesses}")
        print(f"\nHere is the list of the incorrect guesses: {incorrect_guesses}\n")
    
        number_of_incorrect_guesses = len(incorrect_guesses) 
        guesses_left = GUESSES_ALLOWED - number_of_incorrect_guesses

        print(f"You have {guesses_left} guesses left.\n")

        print("----------------------------------------------------------")

        #TODO: check if the game has been won or lost
        if is_word_guessed(secret_word, correct_guesses) is True or number_of_incorrect_guesses == GUESSES_ALLOWED:
            if number_of_incorrect_guesses == GUESSES_ALLOWED:
                print(f"\nSorry you didn't win, try again!\nThe word was: {secret_word}\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
                game_on = False
            else:
                print("\nCongrats, You Won!\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
                game_on = False
                
secret_word = load_word()
secret_word_length = len(secret_word)

spaceman(secret_word)
