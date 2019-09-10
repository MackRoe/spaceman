import random


# initialized variables
secret_word = "boo"
guess = "x"
newstring = ""


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


def is_word_guessed(secret_word, letters_guessed):
    # A function that checks if all the letters of the secret word have been guessed.
    # Args:
        # secret_word (string): the random word the user is trying to guess.
        # letters_guessed (list of strings): list of letters that have been guessed so far.
    # Returns:
    if list(secret_word) == letters_guessed:
        bool = True

        print("You have correctly guessed the word. You win!")
        return bool
    else:
        bool = False

        print("You have not guessed the word. Please guess another letter")
        return bool
        # bool: True only if all the letters of secret_word are in letters_guessed, False otherwise

# TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed

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

    # test
    print("-- get_guessed_word --")
    print(secret_word)
    print(letters_guessed)
    print("-- -- -- -- -- -- -- --")


    cat_string = ""

    for letter in secret_word:
        if letter in letters_guessed:
            cat_string += letter
        else:
            cat_string += "_"


    return cat_string


def is_guess_in_word(guess, secret_word):
    # tests
    print(" ")
    print("-- begin is_guess_in_word function--")
    print(str(guess) + " is guess")
    print(secret_word + " is secret word")
    print("- -- -- -- -- -- -- -- -- - ")

    for letter in secret_word:
        if letter == guess:
            print("")
            print("Your guess of " + guess + " is correct.")
            print("")
            return True

    print("Wrong guess")
    return False

# --- nonfunctional code commented out ---
#    if str(guess) in word_letters:
#        print(str(guess) + " is a correct guess")
#        bool = True
#        return bool
#    else:
#        print("Sorry, but no. That letter is not in the word.")
#        bool = False
#        return bool


    # A function to check if the guessed letter is in the secret word
    # Args:
        # guess (string): The letter the player guessed this round
        # secret_word (string): The secret word -- ## replaced with word_letters
    #Returns:
        # bool: True if the guess is in the secret_word, False otherwise

#TODO: check if the letter guess is in the secret word




def gameplay(secret_word, guess):
    # words exceeding seven letters in length have been relocated
    # new file: words-over-seven-letters
    letters_guessed = []
    running = True
    while running == True:
        guess = input("What letter would you like to guess? ")
        letters_guessed += guess
        if len(guess) > 1:
           print("Please guess only one letter")
        else:
           print("Checking to see if letter is in word")
           print("...")
        # bool cannot start as false
        if is_guess_in_word(guess, secret_word):
            display = get_guessed_word(secret_word, letters_guessed)
            print("Good guess! What next?")
            print(display)
        else:
            print("Wrong.")

        running = not is_word_guessed(secret_word, letters_guessed)
        # bool


def spaceman(secret_word):
    #secret_word = load_word()

    # test
    # load_word(secret_word)

    # print(secret_word)
    # end test
    play = input("Would you like to play a game? [Y or N] ")
    print("Your response was: " + str(play))
    if play.upper() == "Y":
        print("It's on!")
        guess = " "
        print("Welcome to the Game of Spaceman")
        print("You have up to 7 wrong guesses in which to guess ")
        print("a random secret word")
        gameplay(secret_word, guess)

    else:
        print("Input fail. Have a great day.")
    # A function that controls the game of spaceman. Will start spaceman in
    # the command line.
    # Args:
      # secret_word (string): the secret word to guess.

#TODO: show the player information about the game according to the project
# spec
#TODO: Ask the player to guess one letter per round and check that it is only
# one letter
#TODO: Check if the guessed letter is in the secret or not and give the player
# feedback
#TODO: show the guessed word so far
#TODO: check if the game has been won or lost
#These function calls that will start the game




    #    letters_guessed = letters_guessed.extend(guess)
    #    print("So far you have guessed: " + str(letters_guessed))
    #    print(" ")



secret_word = load_word(secret_word)

# test to # DEBUG:
# print(load_word(secret_word))

spaceman(secret_word)
# changed from "spaceman(load_word())"
