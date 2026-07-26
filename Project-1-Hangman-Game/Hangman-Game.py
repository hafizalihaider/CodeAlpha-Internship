"""
==============================================================================
                                HANGMAN GAME
==============================================================================

Description:
------------
Hangman is a simple word guessing game played in the terminal.
The program randomly selects a word from a predefined list, and the
player has to guess the word one letter at a time.

Game Rules:
-----------
1. A random word is selected from the word list.
2. The player has six attempts to guess the word.
3. Only one alphabet letter can be entered at a time.
4. Previously guessed letters cannot be guessed again.
5. Every incorrect guess decreases the remaining attempts.
6. The player wins by guessing all the letters before running out of attempts.

Features:
---------
• Random word selection
• Input validation
• Duplicate letter detection
• Six-attempt limit
• Win and lose conditions
• Displays the correct word after losing


Author       : Muhammad Ali Haider
Language     : Python
Version      : 3.14.6
Date         : 5 July 2026
==============================================================================
"""

import random

# ---------------------------------------------------------------------------
# Display the game title
# ---------------------------------------------------------------------------
print("-" * 50)
print("\n\t\t   HANGMAN GAME\n")
print("-" * 50)

# List of words available for the game
guess_words = ['STARK', 'STEVE', 'PARKER', 'ODINSON', 'HULK']

# Randomly select one word from the list
selected_word = random.choice(guess_words)

print("Guess the word:\n")

# ---------------------------------------------------------------------------
# Display the hidden word using underscores
# ---------------------------------------------------------------------------
for char in selected_word:

    # Print spaces directly if the word contains them
    if char == " ":
        print(char, end=" ")

    # Hide letters using underscores
    else:
        print("_", end=" ")

# Stores every letter guessed by the player
guessed = ""

# Total number of attempts allowed
attempts = 6

# Display the initial number of attempts
print("\n\n", attempts, "Attempt(s) Left!")

# ---------------------------------------------------------------------------
# Main game loop
# ---------------------------------------------------------------------------
while True:

    # Counts the number of letters that are still hidden
    count = 0

    print("\n")

    # Take input from the player and convert it to uppercase
    guess_letter = input("Enter the letter: ").upper()

    print("\n")

    # -----------------------------------------------------------------------
    # Validate the user's input
    # Accept only one alphabet letter
    # -----------------------------------------------------------------------
    if guess_letter.isalpha() and len(guess_letter) == 1:

        # Check whether the letter has already been guessed
        if guess_letter in guessed:
            print("You already guessed", guess_letter, ". Try another letter.\n")
            print("\n\n", attempts, "Attempt(s) Left!")
            continue

        # Save the guessed letter
        guessed += guess_letter

        # -------------------------------------------------------------------
        # Display the current progress of the word
        # -------------------------------------------------------------------
        for char in selected_word:

            # Reveal correctly guessed letters
            if char in guessed:
                print(char, end=" ")

            # Keep unguessed letters hidden
            else:
                count += 1
                print("_", end=" ")

        # Reduce attempts for an incorrect guess
        if guess_letter not in selected_word:
            print("\n\nWrong guess! Try again.")
            attempts -= 1

        # Display remaining attempts
        print("\n", attempts, "Attempt(s) Left!")

        # -------------------------------------------------------------------
        # Check if the player has used all attempts
        # -------------------------------------------------------------------
        if attempts == 0:
            print("\nI'm Sorry. You Lost!")
            print("\nThe word was:", selected_word)
            print("-" * 50)
            break

        # -------------------------------------------------------------------
        # Check if the player has guessed the complete word
        # -------------------------------------------------------------------
        elif count == 0:
            print("\n\n\tCongratulations! You guessed the word.")
            print("-" * 50)
            break

    # -----------------------------------------------------------------------
    # Handle invalid input
    # -----------------------------------------------------------------------
    else:
        print("Please enter exactly one alphabet letter (A-Z).")
        continue