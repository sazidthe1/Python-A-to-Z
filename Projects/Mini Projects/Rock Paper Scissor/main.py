# This is Rock Paper Scissors Game

from random import randint

play_options = ['rock', 'paper', 'scissors']

while True:
    computer_play = play_options[randint(0, 2)] # play option for computer
    user_play = input('Rock, Paper, Scissors? ').lower()   # play option for user

    if computer_play == user_play:
        print("It's a tie!")
    elif user_play == 'rock':   # computer played either paper or scissors
        if computer_play == 'paper':
            print('You lose.', computer_play, 'beats', user_play)
        else:   # scissors
            print('You win!', user_play, 'beats', computer_play)
    elif user_play == 'paper':   # computer played either rock or scissors
        if computer_play == 'scissors':
            print('You lose.', computer_play, 'beats', user_play)
        else:   # rock
            print('You win!', user_play, 'beats', computer_play)
    elif user_play == 'scissors':   # computer played either paper or rock
        if computer_play == 'paper':
            print('You win!', user_play, 'beats', computer_play)
        else:   # rock
            print('You lose.', computer_play, 'beats', user_play)
    else:
        print('Not a valid play option. Try agin!')
        