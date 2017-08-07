import sys, random, math, pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Cirle Demo")
screen.fill((0, 0, 100))

pos_x = 300
pos_y = 250

radius = 200
angle = 360

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        pygame.quit()
        sys.exit()

    angle += 1
    if angle >= 360:
        angle = 0
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = r, g, b

    x = math.cos(math.radians(angle)) * radius
    y = math.sin(math.radians(angle)) * radius

    pos = (int(pos_x + x), int(pos_y + y))
    pygame.draw.circle(screen, color, pos, 10, 0)

    #pos2 = (int(pos_x + x - 20), int(pos_y + y - 20))
    #screen.set_at(pos2,color)  #draw point
    pygame.display.update()
