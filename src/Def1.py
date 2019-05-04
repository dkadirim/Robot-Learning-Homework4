import numpy
import cv2
import random
import copy

def Gui():
    
    gui_size = [500,500]
    gui = numpy.zeros([500,500,3])

    gui[:,:,0] = numpy.ones(gui_size)*240.0
    gui[:,:,1] = numpy.ones(gui_size)*240.0
    gui[:,:,2] = numpy.ones(gui_size)*240.0

    Grid = int(input("Size of the Grid for the game: "))
    states = []
    Square_position = []
    for i in range(Grid + 1):
        for j in range(Grid + 1):
            if Grid%2 == 0:
                gui = cv2.circle(gui,((250 + 50*int(Grid/2)) - i*50,(250 + 50*int(Grid/2)) - j*50), 3, (0,0,0), -1)
                states.append(((250 + 50*int(Grid/2)) - i*50,(250 + 50*int(Grid/2)) - j*50))
            else:
                gui = cv2.circle(gui,((250 + 50*int(Grid/2)+25) - i*50,(250 + 50*int(Grid/2)+25) - j*50), 3, (0,0,0), -1)
                states.append(((250 + 50*int(Grid/2)+25) - i*50,(250 + 50*int(Grid/2)+25) - j*50))

    for i in states:
        a,b = i[0]+25,i[1]+25
        if a < (250 + 50*int(Grid/2)+25) and b < (250 + 50*int(Grid/2)+25):
            Square_position.append((a,b))

    gui_clone = gui.copy()

    for i in states:
        gui = cv2.circle(gui,i, 9, (0,0,0), -1)

    gui = cv2.addWeighted(gui_clone, 0.7, gui, 0.3, 0)

    cv2.imwrite('Dots_Boxes.jpg', gui)
    
    return states,Square_position,Grid 

#states,Square_position,Grid = Gui()