''' Python Project: Hangman '''

import random
from collections import Counter

sports = '''football soccer rugby basketball baseball cricket golf 
            hockey racing swimming'''

food = '''pasta hamburgers hotdogs cereal toast steak chicken apples
            oranges oatmeal pretzels salad'''

videoGames = '''halo cod bioshock pokemon valorant mario destiny titanfall 
                madden minecraft roblox skyrim starfield'''

##def chose_a_category():
category = str(input('What category would you like: sports, food, or games? '))
if category == 'sports':
    randomSport = sports.split(' ')
    word = random.choice(randomSport)
elif category == 'food':
    randomFood = food.split(' ')
    word = random.choice(randomFood)
elif category == 'games':
    randomGame = videoGames.split(' ')
    word = random.choice(randomGame)
else:
    print('Please enter a listed category')
    chose_a_category()

if __name__ == '__main__':
    ##word = chose_a_category()

    for letter in word:
        print('_', end='_')
    print()

    playing = True
    letter_guessed = ''
    chances = len(word) + 2
    correct = 0
    gamestate = 0 ##updated to 1 when the game is won
    try:
        while (chances != 0) and gamestate == 0:
            print()
            chances -= 1

            try:
                guess = str(input('Enter a letter: '))
            except:
                print('Please only use letters.')
                continue

            if not guess.isalpha():
                print('Please guess a letter')
                continue
            elif (len(guess) > 1):
                print('Please only guess one letter')
                continue

            if guess in word:
                guess_occurence = word.count(guess)
                for i in range (guess_occurence):
                    letter_guessed += guess
            
            for char in word:
                if char in letter_guessed and (Counter(letter_guessed) != Counter(word)):
                    print(char, end=' ')
                    correct += 1
                elif (Counter(letter_guessed) == Counter(word)):
                    print(word, end=' ')
                    gamestate = 1
                    print('WooHoo! You have won the game!')
                    break
                    break
                else:
                    print('_', end=' ')
        
        if (chances <= 0) and (Counter(letter_guessed) != Counter(word)):
            print()
            print('Sadly you have been defeated')
            print('The correct answer was {}'.format(word))
    
    except KeyboardInterrupt:
        print()
        print('Sorry you have to go, Have a good day.')
        exit()
