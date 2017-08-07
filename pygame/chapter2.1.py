import pygame
from pygame.locals import *
import sys

pygame.init()
screen = pygame.display.set_mode((600,500))
myfont = pygame.font.Font(None,60)
white = 255,255,255
blue = 0, 0, 255
textImage = myfont.render("Hello Pygame", True, white)
screen.fill(blue)
screen.blit(textImage, (100,100))
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            pygame.quit()
            sys.exit()
