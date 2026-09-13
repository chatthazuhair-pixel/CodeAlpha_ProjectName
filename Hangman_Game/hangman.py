
import random

# A small list of words that the computer can choose from
words = ["python", "computer", "programming", "student", "developer"]

# Randomly choose one word from the list
word = random.choice(words)

# This list will store the letters guessed by the player
guessed_letters = []

# Keep track of how many incorrect guesses the player has made
wrong_guesses = 0

# The game continues while the player has fewer than 6 wrong guesses
while wrong_guesses < 6:
    display = ""

    # Go through each letter of the secret word
    for letter in word:
        # If the player has guessed this letter, show it
        if letter in guessed_letters:
            display += letter
        else:
            # Otherwise, hide the letter with an underscore
            display += "_"

    # Show the current progress of the word
    print("\nWord:", display)
    print("Wrong guesses:", wrong_guesses, "/ 6")

    # If there are no underscores left, the player has guessed the word
    if "_" not in display:
        print("You won!")
        break

    # Ask the player for a letter and convert it to lowercase
    guess = input("Guess a letter: ").lower()

    # Don't allow the player to guess the same letter twice
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Add the new guess to our list
    guessed_letters.append(guess)

    # Check whether the guessed letter is in the secret word
    if guess not in word:
        wrong_guesses += 1
        print("Wrong guess!")
    else:
        print("Correct guess!")

# If the player reaches 6 wrong guesses, they lose
if wrong_guesses == 6:
    print("You lost!")
    print("The word was:", word)

