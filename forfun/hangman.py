from random import random

# import requests

# response = requests.get("https://random-word-api.vercel.app/api?words=1")
# wordtoguess = response.json()[0]

# Words to guess
words=["apple", "banana", "cherry", "date",
       "elderberry", "cherry","grape",
       "lemon", "mango", "nectarine"]

# Select one of the words from the list
wordtoguess = words[int(random() * len(words))]

# Some variables to keep track of the game state
guesses = {}
incorrect = {}
correct = {}
guessed = False

# Unique letters in the word to guess
allletters = {}
for letter in wordtoguess:
    allletters[letter] = 1

# The hangman image as a list
hangmanimage = [
    "------",
    """|
|
|
|
|
------""",
    """------------
|
|
|
|
|
------""",
    """------------
|          |
|
|
|
|
------""",
"""------------
|          |
|          O
|
|
|
------""",
"""------------
|          |
|          O
|          |
|
|
------""",
"""------------
|          |
|          O
|          |--
|
|
------""",
"""------------
|          |
|          O
|        --|--
|
|
------""",
"""------------
|          |
|          O
|        --|--
|         /
|
------""",
"""------------
|          |
|          O
|        --|--
|         / \\
|
------"""
]

# print(wordtoguess)

# The main game loop
while len(incorrect.keys()) < len(hangmanimage)-1:
    guess=input("Enter a letter: ").lower()

    # Assign the letter to the guesses
    guesses[guess]=1

    # Check if the guess is correct or incorrect
    if guess in wordtoguess:
        correct[guess] = 1
    else:
        incorrect[guess] = 1
        
    # Display the letters correctly guessed so far
    for letter in wordtoguess:
        if letter in guesses:
            print(letter, end="")
        else:
            # Display _ for unguessed letters
            print("_", end="")

    print()

    # Show all the letters guessed so far
    print(f"{list(guesses.keys())} guessed so far")
    # print(f"Correct letters: {list(correct.keys())} vs {list(allletters.keys())} in the word")

    # If all letters have been guessed, the game is won
    if len(allletters.keys()) == len(correct.keys()):
        guessed=True
        break

    # Show the state of the condemned
    print(hangmanimage[len(incorrect.keys())])

if guessed:
    print("Congratulations! You guessed the word!")
    print(f"You took {len(guesses)} guesses to get it right.")
else:
    print(f"Game over! The word was: {wordtoguess}")
