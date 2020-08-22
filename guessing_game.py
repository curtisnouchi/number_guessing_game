"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
    print("/////////////////////////////////////\n************************************\nWelcome to the number guessing game!\n************************************\n////////////////////////////////////")
    magic_number = random.randint(1,50)
    attempts = 0
    while True:
        guess = int(input("Guess a number between 1 and 50:  "))
        attempts = attempts + 1
        if guess > magic_number:
            print("It's lower.")
            continue
        elif guess < magic_number:
            print("It's higher.")
            continue
        elif guess == magic_number:
            print("Congratulations! You guessed the number!\nIt took you {} tries!\nGoodbye and thank you for playing! See you next time!\n**********\n********\n******\n****\n**".format(attempts))
            break

start_game()