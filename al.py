from tkinter import*
import tkinter.font as font
import random

player_score=0
computer_score=0
options=[("rock",0),("paper",1),("scissors",2)]

def computer_wins():
    global computer_score,player_score
    computer_score+=1
    winner_label.config(text= "Computer Won!!")
    computerscoreL.config(text= "computer score:"+str(computer_score))
    playerscoreL.config(text= "player score"+str(player_score))


def player_wins():
    global computer_score,player_score
    computer_score+=1
    winner_label.config(text= "player Won!!")
    computerscoreL.config(text= "computer score:"+str(computer_score))
    playerscoreL.config(text= "player score"+str(player_score))


def player_choice(player_input):
    global player_score,computer_score
    print(player_input)
    computer_input=get_computer_choice()
    print(computer_input)

