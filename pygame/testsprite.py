import pygame
from pygame.locals import *
from MySprite import *
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption("Sprite Animation Demo")
font = pygame.font.Font(None, 18)
framerate = pygame.time.Clock()

dragon = MySprite(screen)
dragon.load("dragon.png", 260, 150, 3)
group = pygame.sprite.Group()
group.add(dragon)

while True:
    framerate.tick(20)
    ticks = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            pygame.quit()
            sys.exit()
    screen.fill((0, 0, 100))
    group.update(ticks)
    group.draw(screen)
    print_text(font, 0, 0, "Sprite: " + str(dragon))
    pygame.display.update()