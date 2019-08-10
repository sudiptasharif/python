# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guessed_word = []
    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word.append(letter)
        else:
            guessed_word.append("_ ")
    return "".join(guessed_word)


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters = string.ascii_lowercase
    letters = list(letters)
    for letter in letters_guessed:
        if letter in letters:
            letters.remove(letter)
    return "".join(letters)


def hangman(secret_word):
    """
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    game_stat = {"secret_word": secret_word, "letters_guessed": [], "guesses_remaining": 6,
                 "warnings_remaining": 3, "guessed_letter": "", "keep_playing": True}

    display_game_intro(game_stat["secret_word"], game_stat["warnings_remaining"])
    while game_stat["keep_playing"]:
        display_game_status(game_stat["guesses_remaining"], game_stat["letters_guessed"])
        game_stat["guessed_letter"] = get_guessed_letter()
        play_a_round(game_stat)
        check_game_termination(game_stat)


def check_game_termination(game_stat):
    if game_stat["guesses_remaining"] <= 0:
        game_lost_event(game_stat["secret_word"])
        game_stat["keep_playing"] = False
    elif is_word_guessed(game_stat["secret_word"], game_stat["letters_guessed"]):
        game_won_event(game_stat["secret_word"], game_stat["guesses_remaining"])
        game_stat["keep_playing"] = False


def print_dashes():
    print("-------------")


def display_game_intro(secret_word, warnings_remaining):
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print("You have " + str(warnings_remaining) + " warnings left.")


def display_game_status(guesses_remaining, letters_guessed):
    print_dashes()
    print("You have " + str(guesses_remaining) + " guesses left.")
    print("Available letters: " + get_available_letters(letters_guessed))


def get_guessed_letter():
    guessed_letter = input("Please guess a letter: ")
    return guessed_letter.lower()


def game_lost_event(secret_word):
    print_dashes()
    print("Sorry, you ran out of guesses. The word was " + secret_word + ".")


def game_won_event(secret_word, guesses_remaining):
    unique_letters = len(set(secret_word))
    score = guesses_remaining * unique_letters
    print_dashes()
    print("Congratulations, you won!")
    print("Your total score for this game is: " + str(score))


def play_a_round(game_stat):
    if game_stat["guessed_letter"].isalpha():
        valid_letter_event(game_stat)
    else:
        add_guessed_letter(game_stat["guessed_letter"], game_stat["letters_guessed"])
        invalid_letter_event(game_stat)


def valid_letter_event(game_stat):
    if game_stat["guessed_letter"] in game_stat["letters_guessed"]:
        already_guessed_event(game_stat)
    else:
        add_guessed_letter(game_stat["guessed_letter"], game_stat["letters_guessed"])
        not_guessed_event(game_stat)


def invalid_letter_event(game_stat):
    error_msg = "Oops! That is not a valid letter."
    game_rule_violated_event(game_stat, error_msg)


def game_rule_violated_event(game_stat, error_msg):
    guessed_word = get_guessed_word(game_stat["secret_word"], game_stat["letters_guessed"])

    if game_stat["warnings_remaining"] > 0:
        game_stat["warnings_remaining"] -= 1
        print(error_msg + " You have " + str(game_stat["warnings_remaining"]) + " warnings left: " + guessed_word)
    else:
        game_stat["guesses_remaining"] -= 1
        print(error_msg + " You have no warnings left so you lose one guess: " + guessed_word)


def already_guessed_event(game_stat):
    error_msg = "Oops! You've already guessed that letter."
    game_rule_violated_event(game_stat, error_msg)


def not_guessed_event(game_stat):
    if game_stat["guessed_letter"] in game_stat["secret_word"]:
        correct_guess_event(game_stat)
    else:
        incorrect_guess_event(game_stat)
        adjust_guess_remaining(game_stat)


def correct_guess_event(game_stat):
    guessed_word = get_guessed_word(game_stat["secret_word"], game_stat["letters_guessed"])
    print("Good guess: " + guessed_word)


def incorrect_guess_event(game_stat):
    guessed_word = get_guessed_word(game_stat["secret_word"], game_stat["letters_guessed"])
    print("Oops! That letter is not in my word: " + guessed_word)


def add_guessed_letter(guessed_letter, letters_guessed):
    letters_guessed.append(guessed_letter)


def adjust_guess_remaining(game_stat):
    vowels = ["a", "e", "i", "o", "u"]
    if game_stat["guessed_letter"] in vowels:
        game_stat["guesses_remaining"] -= 2
    else:
        game_stat["guesses_remaining"] -= 1


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------

def match_with_gaps(my_word, other_word):
    """
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word = my_word.replace(" ", "")
    if len(my_word) != len(other_word):
        return False
    for i in range(len(other_word)):
        if my_word[i] == "_":
            if other_word[i] in my_word:
                return False
        elif my_word[i] != other_word[i]:
            return False
    return True


def show_possible_matches(my_word):
    """
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    possible_matches = ""
    for word in wordlist:
        if match_with_gaps(my_word, word):
            possible_matches += word + " "

    if len(possible_matches) == 0:
        print("No matches found")
    else:
        print(possible_matches)


def hangman_with_hints(secret_word):
    """
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    game_stat = {"secret_word": secret_word, "letters_guessed": [], "guesses_remaining": 6,
                 "warnings_remaining": 3, "guessed_letter": "", "keep_playing": True}

    display_game_intro(game_stat["secret_word"], game_stat["warnings_remaining"])
    while game_stat["keep_playing"]:
        display_game_status(game_stat["guesses_remaining"], game_stat["letters_guessed"])
        game_stat["guessed_letter"] = get_guessed_letter()
        if game_stat["guessed_letter"] == "*":
            display_hint_event(game_stat)
        else:
            play_a_round(game_stat)
        check_game_termination(game_stat)


def display_hint_event(game_stat):
    print("Possible word matches are: ")
    show_possible_matches(get_guessed_word(game_stat["secret_word"], game_stat["letters_guessed"]))


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

    ###############
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 

    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
