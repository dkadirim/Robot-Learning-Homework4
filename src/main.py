#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy
import cv2
import random
import copy
from check import *
from Game import *

states,Square_position,Grid = Gui()

def Turn(Grid):
    nodes = []
    
    if Grid == 2:
        X = ((input("Give a Start Node 'x' in range of (0,2) and 'y' in range of (0,2) ")).split(','))
        nx1 = 200 + 50*int(X[0])
        ny1 = 200 + 50*int(X[1])
        nodes.append((nx1,ny1))
    elif Grid == 3:
        X = ((input("Give a Start Node 'x' in range of (0,3) and 'y' in range of (0,3) ")).split(','))
        nx1 = 175 + 50*int(X[0])
        ny1 = 175 + 50*int(X[1])
        nodes.append((nx1,ny1))
    
    dash = check_lines(nx1,ny1)
    
    nx2,ny2 = -1,-1
    while (nx2,ny2) not in dash:
        if Grid == 2:
            X = ((input("Give a End Node 'x' in range of (0,2) and 'y' in range of (0,2) ")).split(','))
            nx2 = 200 + 50*int(X[0])
            ny2 = 200 + 50*int(X[1])
        elif Grid == 3:
            X = ((input("Give a End Node 'x' in range of (0,3) and 'y' in range of (0,3) ")).split(','))
            nx2 = 175 + 50*int(X[0])
            ny2 = 175 + 50*int(X[1])
        
    nodes.append((nx2,ny2))
    return nodes
        
def check_lines(x,y):
    
    L = set()

    x1 = x - 50
    x2 = x + 50
    y1 = y - 50
    y2 = y + 50
    
    [L.add((item[0],y)) for item in states if item[0] == x1]
    [L.add((item[0],y)) for item in states if item[0] == x2]
    [L.add((x,item[1])) for item in states if item[1] == y1]
    [L.add((x,item[1])) for item in states if item[1] == y2]

    return L        

def replay():
    
    replay = input("Do you want to play again. Say yes or no: ")
    
    while replay == 'yes' or replay == 'no':
        if replay == 'yes':
            return True
        elif replay == 'no':
            return False
        
class Player:
    
    def __init__(self, color, score = 0,turn = None):
        self.color = color
        self.score = score
        self.turn = turn

        
def Play():
    while True:
        print('player1 choose your color')
        P1_color,P2_color = Player_color()

        P1 = Player(P1_color)
        P2 = Player(P2_color)

        fp = first_player()
        print("{fp} will go first, randomly choosen") 
        if P1.color == fp:
            P1.turn = True
            P2.turn = False
        else:
            P1.turn = False
            P2.turn = True

        seen = set()
        while win_check(Square_position):

            if P1.turn == True:
                P1.turn = False
                P2.turn = True

                print('{P1_color} choose your move')
                line = Turn(Grid)
                if str(line) not in seen:
                    seen.add(str(line))
                    draw_line(line[0],line[1],P1.color)
                else:
                    P1.turn = True
                    P2.turn = False
                    print("Already Occupied")

                if check_squares(Square_position,P1.color):
                    P1.score += 1
                    P1.turn = True
                    P2.turn = False
                    if check_squares(Square_position,P1.color):
                        P1.score += 1
                        P1.turn = True
                        P2.turn = False



            elif P2.turn == True:
                P1.turn = True
                P2.turn = False

                print('{P2_color} choose your move')
                line = Turn(Grid)
                if str(line) not in seen:
                    seen.add(str(line))
                    draw_line(line[0],line[1],P2.color)
                else:
                    P1.turn = False
                    P2.turn = True
                    print("Already Occupied")

                if check_squares(Square_position,P2.color):
                    P2.score += 1
                    P1.turn = False
                    P2.turn = True
                    if check_squares(Square_position,P2.color):
                        P2.score += 10,0
                        
                        P1.turn = False
                        P2.turn = True

        if P1.score > P2.score:
            print('P1 Score',P1.score)
            print('P2 Score',P2.score)
            print('{P1.color} has won the game')
        elif P2.score > P1.score:
            print('P1 Score',P1.score)
            print('P2 Score',P2.score)
            print('{P2.color} has won the game')
        else:
            print('P1 Score',P1.score)
            print('P2 Score',P2.score)
            print('Game Tied')

        if replay():
            continue
        else:
            print('Good Bye')

        break

Play()            


# In[ ]:




