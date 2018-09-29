#!/usr/bin/env python3
"""evelandy/W.G.
Sept. 29 2018 3:20pm
Rock Paper Scissors
Python36-32 
"""
import random
import time
import os


CHOICES = ['Rock', 'Paper', 'Scissors']


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


while True:
    print("To quit press (q)")
    user_choice = input("Rock, Paper or Scissors? ")
    pc_choice = random.choice(CHOICES)

    if user_choice.lower() == 'q':
        print("Thank You For Playing Come Back Soon!")
        break

    print("Ready")
    time.sleep(1)
    print("Set")
    time.sleep(1)
    print("Go!")
    print("You Chose: {} \nPC Chose: {}".format(user_choice, pc_choice))

    if user_choice.lower() == pc_choice.lower():
        print("Tie!")
        answer = input("Would You Like To Play Again? (y/n)")
        if answer.lower() == 'n':
            print("See You Next Time!")
            break
        else:
            clear()
    elif user_choice.lower() == 'rock' and pc_choice.lower() == 'scissors':
        print("You Win!")
        answer = input("Would You Like To Play Again? (y/n)")
        if answer.lower() == 'n':
            print("See You Next Time!")
            break
        else:
            clear()
    elif user_choice.lower() == 'paper' and pc_choice.lower() == 'rock':
        print("You Win!")
        answer = input("Would You Like To Play Again? (y/n)")
        if answer.lower() == 'n':
            print("See You Next Time!")
            break
        else:
            clear()
    elif user_choice.lower() == 'scissors' and pc_choice.lower() == 'paper':
        print("You Win!")
        answer = input("Would You Like To Play Again? (y/n)")
        if answer.lower() == 'n':
            print("See You Next Time!")
            break
        else:
            clear()
    elif user_choice.lower() == 'rock' and pc_choice.lower() == 'paper':
        print("You loose...")
        answer = input("Would You Like To Play Again? (y/n)")
        if answer.lower() == 'n':
            print("See You Next Time!")
            break
        else:
            clear()
    elif user_choice.lower() == 'paper' and pc_choice.lower() == 'scissors':
        print("You loose...")
        answer = input("Would You Like To Play Again? (y/n)")
        if answer.lower() == 'n':
            print("See You Next Time!")
            break
        else:
            clear()
    elif user_choice.lower() == 'scissors' and pc_choice.lower() == 'rock':
        print("You loose...")
        answer = input("Would You Like To Play Again? (y/n)")
        if answer.lower() == 'n':
            print("See You Next Time!")
            break
        else:
            clear()
    else:
        print("Sorry You Didn't Choose Rock, Paper, Or Scissors... Try again...")
