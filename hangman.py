''' Python Project: Hangman '''

import random
from collections import Counter

sports = '''football soccer rugby basketball baseball cricket golf 
            hockey racing swimming'''

food = '''pasta hamburgers hotdogs cereal toast steak chicken apples
            oranges oatmeal pretzels salad'''

videoGames = '''halo cod bioshock pokemon valorant mario destiny titanfall 
                madden minecraft roblox skyrim starfield'''

def chose_a_category():
    category = str(input('What category would you like: sports, food, or games? '))
    if category == 'sports':
        print("You have selected Sports")
        randomSport = sports.split(' ')
        word = random.choice(randomSport)
    elif category == 'food':
        print("You have selected Food")
        randomFood = food.split(' ')
        word = random.choice(randomFood)
    elif category == 'games':
        print("You have selected Video Games")
        randomGame = videoGames.split(' ')
        word = random.choice(randomGame)
    else:
        print('Please enter a listed category')
        chose_a_category()
    return word

def gamePlay():
    word = chose_a_category()
    letter_guessed = ''
    prior_guesses = []
    chances = len(word) + 2
    correct = 0
    gamestate = 0 ##updated to 1 when the game is won

    for letter in word:
        print('_', end=' ')
    print()

    while (chances != 0) and gamestate == 0:
        print()
        print('You have {}'.format(chances), ' guesses remaining.')
        chances -= 1
        try:
            guess = str(input('Enter your guess: '))
        except:
            print('Please only use letters.')
            continue

        ## check for a proper guess, must be an alphabetic character with length of 1
        if not guess.isalpha():
            print('Please guess an alphabertic character')
            continue
        elif (len(guess) > 1):
            print('Please only guess one letter')
            continue
        elif guess in prior_guesses:
            print('You have already guessed this letter')
            #chances += 1 ##uncomment for easier gameplay 
            continue
        else:
            prior_guesses.append(guess)
        
        ## what to do if user's guess was correct
        if guess in word:
            guess_occurence = word.count(guess)
            for i in range (guess_occurence):
                letter_guessed += guess
        
        ## printing the updated gamestate (the word with the correctly guessed letter filled in)
        for char in word:
            if char in letter_guessed and (Counter(letter_guessed) != Counter(word)):
                print(char, end=' ')
                correct += 1
            elif (Counter(letter_guessed) == Counter(word)):
                print()
                print(word, end=' ')
                gamestate = 1
                print('WooHoo! You have won the game!')
                break
                break
            else:
                print('_', end=' ')
    
    ## if the user has used all their guesses
    if (chances <= 0) and (Counter(letter_guessed) != Counter(word)):
        print()
        print('Sadly you have been defeated')
        print('The correct answer was {}'.format(word))


if __name__ == '__main__':
    gamePlay()
