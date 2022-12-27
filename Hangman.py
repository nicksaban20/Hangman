import os
from Hangman.words import cleanWordList
import random

os.system('clear')

HANGMANPICS = ['''
    +---+
    |   |
        |
        |
        |
        |
   =========''','''
    +---+
    |   |
    o   |
        |
        |
        |
   =========''','''
    +---+
    |   |
    o   |
    |   |
        |
        |
   =========''','''
    +---+
    |   |
    o   |
   /|   |
        |
        |
   =========''','''
    +---+
    |   |
    o   |
   /|\  |
        |
        |
   =========''','''
    +---+
    |   |
    o   |
   /|\  |
   /    |
        |
   ========''','''
    +---+
    |   |
    o   |
   /|\  |
   / \  |
        |
   ========''']

print("""
 /$$   /$$                                                                
| $$  | $$                                                                
| $$  | $$  /$$$$$$  /$$$$$$$   /$$$$$$  /$$$$$$/$$$$   /$$$$$$  /$$$$$$$ 
| $$$$$$$$ |____  $$| $$__  $$ /$$__  $$| $$_  $$_  $$ |____  $$| $$__  $$
| $$__  $$  /$$$$$$$| $$  \ $$| $$  \ $$| $$ \ $$ \ $$  /$$$$$$$| $$  \ $$
| $$  | $$ /$$__  $$| $$  | $$| $$  | $$| $$ | $$ | $$ /$$__  $$| $$  | $$
| $$  | $$|  $$$$$$$| $$  | $$|  $$$$$$$| $$ | $$ | $$|  $$$$$$$| $$  | $$
|__/  |__/ \_______/|__/  |__/ \____  $$|__/ |__/ |__/ \_______/|__/  |__/
                               /$$  \ $$                                  
                              |  $$$$$$/                                  
                               \______/                                 """)


print("Press Enter to Play!")
temp = input()
os.system('clear')

print(HANGMANPICS[0])
chosenWord = random.choice(cleanWordList)

string = ''
length = len(chosenWord)

print(chosenWord)

for i in range(length):
    string += '_ '

print(string)

lives = len(HANGMANPICS) - 1

splitWord = []
guessList = []
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
usedLetters = []

for letter in chosenWord:
    guessList.append('_ ')

for letter in chosenWord:
    splitWord.append(letter)

while lives > 0:
    guess = input('Guess a letter: ')

    if len(guess) == 1 and guess in letters and guess not in usedLetters:
        usedLetters.append(guess)

        if chosenWord.count(guess) == 1:

            if guess in splitWord:
                guessIndex = splitWord.index(guess)
                guessList[guessIndex] = guess
                guessedLetters = ''

                for letter in guessList:
                    guessedLetters += letter
                    os.system('clear')

                print(HANGMANPICS[len(HANGMANPICS) - 1 - lives])
                print(guessedLetters)

                if chosenWord == guessedLetters:
                    os.system('clear')
                    print("Congrats, you guessed the word!")
                    break


            else:
                os.system('clear')
                lives -= 1
                print(HANGMANPICS[len(HANGMANPICS) - 1 - lives])
                print(guessedLetters)
            
            if lives == 0:
                print("You ran out of lives!")
                print("The word was " + chosenWord)

        else:
            if guess in splitWord:
                guessIndex = splitWord.index(guess)
                guessList[guessIndex] = guess
                guessedLetters = ''

                for letter in guessList:
                    guessedLetters += letter

            if guess in splitWord:
                guessIndex = splitWord.index(guess, guessIndex + 1)
                guessList[guessIndex] = guess
                guessedLetters = ''

                for letter in guessList:
                    guessedLetters += letter
                    os.system('clear')



            print(HANGMANPICS[len(HANGMANPICS) - 1 - lives])
            print(guessedLetters)

    else:
        os.system('clear')
        print(HANGMANPICS[len(HANGMANPICS) - 1 - lives])
        print(guessedLetters)
        print("Your guess has to be 1 unused letter!")