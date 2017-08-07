import pygame
from pygame.locals import *
import sys
import math
white = 255,255,255
blue = 0, 0, 200
pos_x = 300
pos_y = 250
vel_x = 2
vel_y = 1
pygame.init()
screen = pygame.display.set_mode((600,500))
myfont = pygame.font.Font(None,60)

textImage = myfont.render("Hello Pygame", True, white)

while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            pygame.quit()
            sys.exit()
 
    #chapter2
    pygame.display.set_caption("Drawing start")
    screen.fill(blue)
    #'''   
    #chapter2.2
    screen.blit(textImage, (100,100))
    ####
        
    #chapter2.3
    color = 255,255,0
    position = 300,250
    radius = 100
    width = 10
    pygame.draw.circle(screen,color,position,radius,width)
    #####
    #'''
    
    #chapter2.4
    pos_x += vel_x
    pos_y += vel_y
    if pos_x > 500 or pos_x < 0:
        vel_x = -vel_x
    if pos_y > 400 or pos_y < 0:
        vel_y = -vel_y
    color = 255,255,0
    pos = pos_x,pos_y,100,100
    width = 0
    pygame.draw.rect(screen,color,pos,width)
    ####

    #chapter2.5
    color = 100,255,200
    width = 8
    pygame.draw.line(screen,color,(440,100),(440,400),width)
    ###

    #chapter2.6
    color = 255,0,255
    position = 480,10,100,400
    start_angle = math.radians(0)
    end_angle = math.radians(180)
    width = 8
    pygame.draw.arc(screen,color,position,start_angle,end_angle,width)
    ####
    
    pygame.display.update()

    
