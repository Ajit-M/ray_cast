import pygame as pg

#Initialize Pygame
pg.init()

#Create a screen
screen = pg.display.set_mode((800,600))

quit_event = True
while quit_event:
    
    #creating an event to quit the screen
    for event in pg.event.get():
        if event.type == "q":
            quit_event = False

