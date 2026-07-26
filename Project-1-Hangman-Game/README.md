# Hangman Game

## Description

Hangman Game is a simple console-based game developed in Python.

The program randomly selects a word from a predefined list, and the player must guess the word one letter at a time before running out of attempts.

---

## Features

- Random word selection
- Input validation
- Duplicate guess detection
- Six attempts to guess the word
- Win and lose conditions
- Displays the correct word after losing
- Simple command-line interface

---

## Technologies Used

- Python 3

---

## Project Structure

```text
Hangman-Game/
│── main.py
│── README.md
```

---


## How to Play

1. The program randomly selects a hidden word.
2. Enter one alphabet letter at a time.
3. Correct guesses reveal the matching letters.
4. Incorrect guesses reduce the remaining attempts.
5. Previously guessed letters cannot be entered again.
6. Guess the complete word before all attempts are used.

---

## Sample Output

```text
--------------------------------------------------

                HANGMAN GAME

--------------------------------------------------

Guess the word:

_ _ _ _ _ _

6 Attempt(s) Left!

Enter the letter: A

A _ _ _ _ _

6 Attempt(s) Left!
```

---

## Future Improvements

- Add Hangman ASCII art
- Add multiple word categories
- Add difficulty levels
- Read words from an external file
- Add a hint system
- Add a score system
- Add a play again option

---

## Author

**Muhammad Ali Haider**

---

## License

This project is created for educational purposes and is free to use and modify.