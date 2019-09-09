import random

#empty list to contain letters (str type variables)  guessed by user
letters_guessed = []

#empty list to contain the list of letters contained in the secret word
word_letters = []

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
    if list(secret_word) == letters_guessed:
        bool = True

        print("You have correctly guessed the word. You win!")
        return bool
    else:
        bool = False

        print("please guess another letter")
        return bool
        # bool: True only if all the letters of secret_word are in letters_guessed, False otherwise

# TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed

def get_guessed_word(secret_word, letters_guessed, guess, newstring):

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

    # # DEBUG:
    print(secret_word)

    guess = input("What letter would you like to guess? ")
    # print to  DEBUG
    print(guess + " is your guess.")
    # guess is a string variable with one item
    if len(guess) > 1:
        print("Please guess only one letter")
    else:
        print("Checking to see if letter is in word")

    letters_guessed.extend(guess)
    print("So far you have guessed: " + str(letters_guessed))
    print(" ")
    # Issue: str(letters_guessed.append(guess) is outputting "None".
    # ... should output the list of all letters guessed
    return letters_guessed, guess


def is_guess_in_word(guess, word_letters, bool):
    print(word_letters)
    if str(guess) in word_letters:
        print("That is a correct guess")


        bool = True
        return bool
    else:
        print("Sorry, but no. That letter is not in the word.")
        bool = False
        return bool


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

    wordlength = len(secret_word)
    blanks_printed = wordlength
    blank = "_"
    blank = blank * wordlength
    print(blank)
    # the * prints repetitions

    get_guessed_word(secret_word, letters_guessed, guess, newstring)

    if is_guess_in_word(letters_guessed, guess, word_letters):

        # add guess to blank at correct index
        # then remove extra item from blank
        letter_index = list.index(word_letters)
        blank.insert(letter_index, guess)
        blank.pop(len(secret_word))
        print(blank)

    get_guessed_word(secret_word, letters_guessed, guess, newstring)
    print("You have guessed " + guess)

    is_guess_in_word(guess, word_letters, bool)

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
