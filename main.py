import random

# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
from hangman_words import word_list
from hangman_art import stages, logo

lives = 6

# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(logo)

word_to_guess = random.choice(word_list)

users_guess = "_" * len(word_to_guess)
print(f"Welcome to Hangman!\n")
print(f"Guess the word: {users_guess}\n")

game_over = False

while not game_over:
    guessed_correctly = False
    redundant_letter = False

    # TODO-6: - Update the code below to tell the user how many lives they have left.
    print("****************************<???>/6 LIVES LEFT****************************".replace("<???>", str(lives)))
    guess = input("Guess a letter: ").lower()

    # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.

    display = ""

    for index, letter in enumerate(word_to_guess):
        if letter == guess:
            if guess in users_guess and not redundant_letter:
                print("You've already guessed: " + guess)
                guessed_correctly = True
                redundant_letter = True
            else:
                guessed_correctly = True
            display += letter
        else:
            display += users_guess[index]

    print("Your guess so far: " + display)
    users_guess = display

    if users_guess == word_to_guess:
        game_over = True
        print("****************************YOU WIN****************************")

    elif not guessed_correctly:
        # TODO-5: - If the letter is not in the word_to_guess, print out the letter and let them know it's not in the word.
        #  e.g. You guessed d, that's not in the word. You lose a life.
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
    if lives == 0:
        # TODO 7: - Update the print statement below to give the user the correct word they were trying to guess.
        game_over = True
        print(f"***********************IT WAS {word_to_guess}! YOU LOSE**********************")

    # TODO-2: - Update the code below to use the stages List from the file hangman_art.py
    print(stages[lives])
