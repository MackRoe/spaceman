import random

letters_guessed = []
word_letters = []
secret_word = "boo"

def load_word(secret_word):
# A function that reads a text file of words and randomly selects one to use as the secret word
        # from the list.
    # Returns:
           # string: The secret word to be used in the spaceman guessing game
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    words_list = words_list[0].split(' ')
    words_list = list(words_list)
    secret_word = random.choice(words_list)

    # print(secret_word)
    return secret_word

# function to split string into list of letters_guessed
def split(secret_word, word_letters):
    word_letters = list(secret_word)
    print(word_letters)
    return word_letters



def is_word_guessed(secret_word, letters_guessed):
    # A function that checks if all the letters of the secret word have been guessed.
    # Args:
        # secret_word (string): the random word the user is trying to guess.
        # letters_guessed (list of strings): list of letters that have been guessed so far.
    # Returns:
    if word_letters == letters_guessed:
        return True
    else:
        return False
        # bool: True only if all the letters of secret_word are in letters_guessed, False otherwise

# TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
# pass (commented out unfamiliar command)
def get_guessed_word(secret_word, letters_guessed):

    # A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    # Args:
        # secret_word (string): the random word the user is trying to guess.
        # letters_guessed (list of strings): list of letters that have been guessed so far.
    # Returns:
        # string: letters and underscores.  For letters in the word that the user has guessed correctly,
        # the string should contain the letter at the correct position.  For letters in the word that the
        # user has not yet guessed, shown an _ (underscore) instead.
#TODO: Loop through the letters in secret word and build a string that shows the letters that have been
    # guessed correctly so far that are saved in letters_guessed and underscores for the letters that have
    # not been guessed yet
    guess = input("What letter would you like to guess? ")
    print(letters_guessed.append(guess))

    return guess


def is_guess_in_word(letters_guessed, guess, word_letters):
    # changed secret_word to word_letters
    # added letters_guessed
    wrong_guess_count = 0
    guesses_left = 7 - wrong_guess_count
    #wrong_guess_count shound be index of letters_guessed
    if guess in word_letters:
        print("You have guessed correctly.")
    else:
        wrong_guess_count += 1
        print("Good try, but that is not one of the letters.")
        print("You have " + str(guesses_left) + " guesses remaining.")
        if wrong_guess_count == 1:
            print(" | ")
        elif wrong_guess_count == 2:
            print(" | ")
            print(" O ")
        elif wrong_guess_count == 3:
            print(" | ")
            print(" O_")
        elif wrong_guess_count == 4:
            print(" | ")
            print("_O_")
        elif wrong_guess_count == 5:
            print(" | ")
            print("_O_")
            print(" | ")
        elif wrong_guess_count == 6:
            print(" | ")
            print("_O_")
            print(" | ")
            print("/  ")
        elif wrong_guess_count == 7:
            print(" | ")
            print("_O_")
            print(" | ")
            print("/ \\")
            print("---")
            print("GAME OVER")




    # A function to check if the guessed letter is in the secret word
    # Args:
        # guess (string): The letter the player guessed this round
        # secret_word (string): The secret word
    #Returns:
        # bool: True if the guess is in the secret_word, False otherwise

#TODO: check if the letter guess is in the secret word

def gameplay(secret_word, guess):
    # words exceeding seven letters in length have been relocated
    # new file: words-over-seven-letters

    # potential logic flaw - while test value is not decreasing
    wordlength = len(secret_word)
    blanks_printed = wordlength
    blank = "_"
    while blanks_printed <= 7:
        blank += blank
        blanks_printed += 1
        print(blank)

    get_guessed_word(secret_word, letters_guessed)

    is_guess_in_word(letters_guessed, guess, word_letters)



    get_guessed_word(secret_word, letters_guessed)
    print("You have guessed {}").format(guess)
    print("...")
    print(blank)
    print("...")
    is_word_guessed(secret_word, letters_guessed)

def spaceman(secret_word):
    #secret_word = load_word()

    # test
    # load_word(secret_word)
    split(secret_word, word_letters)
    print(secret_word)
    # end test
    play = input("Would you like to play a game? [Y or N] ")
    if play == "Y" or "y":
        print("It's on!")
        guess = " "
        gameplay(secret_word, guess)
    # commented out for debug test
    # elif play == "What game?":
    #    print("It's called Spaceman")
    #    print("You get 7 tries to guess all the letters in a random word.")
    #    input("Do you want to play? [Y or N] ")
    #    gameplay()
    else:
        print("Input fail. Have a great day.")
    # A function that controls the game of spaceman. Will start spaceman in the command line.
    # Args:
      # secret_word (string): the secret word to guess.

#TODO: show the player information about the game according to the project spec
#TODO: Ask the player to guess one letter per round and check that it is only one letter
#TODO: Check if the guessed letter is in the secret or not and give the player feedback
#TODO: show the guessed word so far
#TODO: check if the game has been won or lost
#These function calls that will start the game




secret_word = load_word(secret_word)

# test to # DEBUG:
# print(load_word(secret_word))

spaceman(secret_word)
# changed from "spaceman(load_word())"
