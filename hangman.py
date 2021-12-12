import random
from words import word_list
import string


def get_valid_word(words):
    word = random.choice(words)  # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(word_list)
    word_letters = set(word)  # keep trak of the letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    lives = 6

    # Getting user input
    while len(word_letters) > 0 and lives > 0:
        print('You have ', lives, 'left. You have guessed: ',
              ' '.join(used_letters))
        current_list = [
            letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(current_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print('Letter is not in word : (')
        elif user_letter in used_letters:
            print("You have guessed that letter already!")
        else:
            print("Please make sure you type in a character")

    if lives == 0:
        print('You lost! The word was ', word)
    else:
        print('Yay! You won, the word was: ', word)

    return 0


hangman()
