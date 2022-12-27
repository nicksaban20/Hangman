import os
from words import cleanWordList
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

print("""
   _____      _           _      _____                                          _      
  / ____|    | |         | |    / ____|                                        | |     
 | (___   ___| | ___  ___| |_  | |  __  __ _ _ __ ___   ___ _ __ ___   ___   __| | ___ 
  \___ \ / _ \ |/ _ \/ __| __| | | |_ |/ _` | '_ ` _ \ / _ \ '_ ` _ \ / _ \ / _` |/ _ \\
  ____) |  __/ |  __/ (__| |_  | |__| | (_| | | | | | |  __/ | | | | | (_) | (_| |  __/
 |_____/ \___|_|\___|\___|\__|  \_____|\__,_|_| |_| |_|\___|_| |_| |_|\___/ \__,_|\___|
""")
gameMode = input(
    "Select a mode to play in: \n\t1. Single Player \n\t2. Multiplayer \n>")

if gameMode == '1':
    chosenWord = random.choice(cleanWordList)
elif gameMode == '2':
    chosenWord = input(
        "What is the word or phrase to play with in this game: ")
else:
    os.system("clear")
    print("""
.___                    .__  .__    .___   .___                      __   
|   | _______  _______  |  | |__| __| _/   |   | ____ ______  __ ___/  |_ 
|   |/    \  \/ /\__  \ |  | |  |/ __ |    |   |/    \\____ \|  |  \   __\\
|   |   |  \   /  / __ \|  |_|  / /_/ |    |   |   |  \  |_> >  |  /|  |  
|___|___|  /\_/  (____  /____/__\____ |    |___|___|  /   __/|____/ |__|  
         \/           \/             \/           \/|__|                
    """)
    print("Playing as a single player, press enter to continue")
    temp = input()
    chosenWord = random.choice(cleanWordList)

os.system('clear')
print(HANGMANPICS[0])

string = ''
length = len(chosenWord)

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
    if guess == '':
        os.system('clear')
        print("Invalid Input")
        break

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
                print("You have used these letters:")
                print(usedLetters)
                print(HANGMANPICS[len(HANGMANPICS) - 1 - lives])
                print(guessedLetters)

                if chosenWord == guessedLetters:
                    os.system('clear')
                    print("Congrats, you guessed the word!")
                    break

            else:
                os.system('clear')
                lives -= 1
                print("You have used these letters:")
                print(usedLetters)
                print(HANGMANPICS[len(HANGMANPICS) - 1 - lives])
                print(guessedLetters)

        elif chosenWord.count(guess) == 2:
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
            print("You have used these letters:")
            print(usedLetters)
            print(HANGMANPICS[len(HANGMANPICS) - 1 - lives])
            print(guessedLetters)

        elif chosenWord.count(guess) > 2:
            if guess in splitWord:
                guessIndex = splitWord.index(guess)
                guessList[guessIndex] = guess
                guessedLetters = ''

                for letter in guessList:
                    guessedLetters += letter

            for i in range(chosenWord.count(guess) - 2):
                if guess in splitWord:
                    guessIndex = splitWord.index(guess, guessIndex + 1)
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
            print("You have used these letters:")
            print(usedLetters)
            print(HANGMANPICS[len(HANGMANPICS) - 1 - lives])
            print(guessedLetters)

        else:
            os.system('clear')
            lives -= 1
            guessedLetters = ''
            for letter in guessList:
                guessedLetters += letter
                os.system('clear')
            print("You have used these letters:")
            print(usedLetters)
            print(HANGMANPICS[len(HANGMANPICS) - 1 - lives])
            print(guessedLetters)

    else:
        os.system('clear')
        print("You have used these letters:")
        print(usedLetters)
        print(HANGMANPICS[len(HANGMANPICS) - 1 - lives])
        print(guessedLetters)
        print("Your guess has to be 1 unused letter!")

if lives == 0:
    print("You ran out of lives!")
    print("The word was " + chosenWord)
