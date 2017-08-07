import sys, random, math, pygame
from pygame.locals import *

def print_text(font, x, y, text, color=(255, 255, 255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x, y))

def wrap_angle(angle):
    return angle % 360

class Point(object):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x
    def setx(self, x):
        self.__x = x
    x = property(getx, setx)

    def gety(self):
        return self.__y
    def sety(self, y):
        self.__y = y
    y = property(gety, sety)

    def __str__(self):
        return "{X:"+"{:.0f}".format(self.__x) + "{Y:"+"{:.0f}".format(self.__y)

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Orbit Demo")
space = pygame.image.load("space.png").convert_alpha()
ship = pygame.image.load("freelance.png").convert_alpha()
planet = pygame.image.load("planet2.png").convert_alpha()

ship_scale_rate = 3
width,height = ship.get_size()
ship = pygame.transform.scale(ship, (width//ship_scale_rate, height//ship_scale_rate))
ship_smooth = pygame.transform.smoothscale(ship, (width//4, height//4))

radius = 250
angle = 0.0
pos = Point(0, 0)
old_pos = Point(0, 0)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        pygame.quit()
        sys.exit()

    screen.blit(space, (0, 0))
    angle = wrap_angle(angle - 0.1)
    pos.x = math.sin(math.radians(angle)) * radius
    pos.y = math.cos(math.radians(angle)) * radius

    delta_x = (pos.x - old_pos.x)
    delta_y = (pos.y - old_pos.y)
    rangle = math.atan2(delta_y, delta_x)
    rangled = wrap_angle(-math.degrees(rangle))
    scratch_ship = pygame.transform.rotate(ship, rangled)

    width,height = scratch_ship.get_size()
    x = 400 + pos.x - width // 2
    y = 300 + pos.y - width // 2
    screen.blit(scratch_ship, (x, y))

    screen.blit(ship_smooth, (x - 50, y - 50))
    width, height = planet.get_size()
    screen.blit(planet, (400 - width//2, 300 - height // 2))
    pygame.display.update()
    old_pos.x = pos.x
    old_pos.y = pos.y
