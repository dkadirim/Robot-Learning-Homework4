import numpy
import cv2
import random
import copy

def first_player():
    return random.choice(['Blue','Red'])

def Player_color():
    
    P1 = ''
    P2 = ''
    
    while P1 not in ('Red','Blue'):
        P1 = input("Please pick a color 'Red' or 'Blue' ")
        
    if P1 == 'Red':
        P2 = 'Blue'
        print("player1 chose Red and player2 will be Blue")
        return ('Red','Blue')
    else:
        P2 = 'Red'
        print("player1 chose Blue and player2 will be Red")
        return ('Blue','Red')


def draw_line(start,end,color):
    gui = cv2.imread('Dots_Boxes.jpg')
    if color == 'Blue':
        gui = cv2.circle(gui,start, 3, (0,0,0), -1)
        gui = cv2.circle(gui,end, 3, (0,0,0), -1)
        gui = cv2.line(gui,start,end,(200,100,20),3)
        cv2.imwrite('Dots_Boxes.jpg', gui)
    elif color == 'Red':
        gui = cv2.circle(gui,start, 3, (0,0,0), -1)
        gui = cv2.circle(gui,end, 3, (0,0,0), -1)
        gui = cv2.line(gui,start,end,(20,100,200),3)
        cv2.imwrite('Dots_Boxes.jpg', gui)

def win_check(Square_position):
    gui = cv2.imread('Dots_Boxes.jpg')
    flag = True
    for i in Square_position:
        a,b = i
        
        if sum(gui[a][b]) == 720:
            flag = True
            break
        else:
            flag = False
    return flag


def check_squares(Square_position,color):
    gui = cv2.imread('Dots_Boxes.jpg')
    for i in Square_position:
        a,b = i
        
        x1 = a - 25
        x2 = a + 25
        y1 = b - 25
        y2 = b + 25
        if color == 'Blue':
            if sum(gui[x1][b]) in range(0,700) and sum(gui[x2][b]) in range(0,700) and sum(gui[a][y1]) in range(0,700) and sum(gui[a][y2]) in range(0,700) and sum(gui[a][b]) == 720:
                vert = numpy.array([[y1,x1],[y1,x2],[y2,x2],[y2,x1]], numpy.int32)
                gui = cv2.fillPoly(gui,[vert],(255,200,100))
                cv2.imwrite('Dots_Boxes.jpg', gui)
                return True
        elif color == 'Red':
            if sum(gui[x1][b]) in range(0,700) and sum(gui[x2][b]) in range(0,700) and sum(gui[a][y1]) in range(0,700) and sum(gui[a][y2]) in range(0,700) and sum(gui[a][b]) == 720:
                vert = numpy.array([[y1,x1],[y1,x2],[y2,x2],[y2,x1]], numpy.int32)
                gui = cv2.fillPoly(gui,[vert],(100,200,255))
                cv2.imwrite('Dots_Boxes.jpg', gui)
                return True
