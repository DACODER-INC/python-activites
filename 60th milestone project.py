import random
playing = True
number = random.randint(0, 9)
print('I will generate a random number from 0 to 9, and you have to guess the number 1 digit at a time')
print('The game ends when you guess the number correctly or if you want to quit the game you can press ctrl + c')
while playing:
    guess = int(input('Enter your guess: '))
    if guess == number:
        print('You won the game and the number was', number)
        break
    else:
        print('You guessed wrong, try again')

    