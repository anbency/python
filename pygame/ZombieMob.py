#import itertools, sys, time, random, math, pygame
#from pygame.locals import *
from MySprite import *

def cal_velocity(direction, vel = 1.0):
    velocity = Point(0, 0)
    if direction == 0:
        velocity.y = -vel
    elif direction == 2:
        velocity.x = vel
    elif direction == 4:
        velocity.y = vel
    elif direction == 6:
        velocity.x = -vel
    return velocity

def reverse_direction(sprite):
    if sprite.direction == 0:
        sprite.direction = 4
    elif sprite.direction == 2:
        sprite.direction = 6
    elif sprite.direction == 4:
        sprite.direction = 0
    elif sprite.direction == 6:
        sprite.direction = 2

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Collision Demo")
font = pygame.font.Font(None, 36)
time = pygame.time.Clock()

player_group = pygame.sprite.Group()
zombie_group = pygame.sprite.Group()
health_group = pygame.sprite.Group()

player = MySprite()
player.load("farmer walk.png", 96, 96, 8)
player.position = 80, 80
player.direction = 4
player_group.add(player)

zombie_image = pygame.image.load("zombie walk.png").convert_alpha()
for n in range(0, 10):
    zombie = MySprite()
    zombie.load("zombie walk.png", 96, 96, 8)
    zombie.position = random.randint(0, 700), random.randint(0, 500)
    zombie.direction  = random.randint(0,3) * 2
    zombie_group.add(zombie)

health = MySprite()
health.load("health.png", 32, 32, 1)
health.position = 400, 300
health_group.add(health)

game_over = False
player_moving = False
player_health = 100

while True:
    time.tick(30)
    ticks = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        pygame.quit()
        sys.exit()
    elif keys[K_UP]:
        player.direction = 0
        player_moving = True
    elif keys[K_RIGHT]:
        player.direction = 2
        player_moving = True
    elif keys[K_DOWN]:
        player.direction = 4
        player_moving = True
    elif keys[K_LEFT]:
        player.direction = 6
        player_moving = True
    elif keys[K_RETURN]:
        if game_over:
            player.position = 80, 80
            player.direction = 4
            game_over = False
            player_moving = True
            player_health = 100

    if not game_over:
        player.first_frame = player.direction * player.columns
        player.last_frame = player.first_frame + player.columns - 1
        if player.frame < player.first_frame:
            player.frame = player.first_frame
        if not player_moving:
            player.frame = player.first_frame = player.last_frame
        else:
            player.velocity = cal_velocity(player.direction, 1.5)
            player.velocity.x *= 1.5
            player.velocity.y *= 1.6

        player_group.update(ticks, 50)

        if player_moving:
            player.X += player.velocity.x
            player.Y += player.velocity.y
            if player.X < 0: player.X = 0
            elif player.X > 700: player.X = 700
            if player.Y < 0: player.Y = 0
            elif player.Y > 500: player.Y = 500

        zombie_group.update(ticks, 50)

        for z in zombie_group:
            z.first_frame = z.direction * z.columns
            z.last_frame = z.first_frame + z.columns - 1
            if z.frame < z.first_frame:
                z.frame = z.first_frame
                z.velocity = cal_velocity(z.direction)
                z.X += z.velocity.x
                z.Y += z.velocity.y
                if z.X < 0 or z.X > 700 or z.Y < 0 or z.Y > 500:
                    reverse_direction(z)

        attacker = None
        attacker = pygame.sprite.spritecollideany(player, zombie_group)
        if attacker != None:
            if pygame.sprite.collide_rect_ratio(0.5)(player, attacker):
                player_health -= 10
                if attacker.X < player.X:
                    attacker.X -= 10
                elif attacker.X > player.X:
                    attacker.X += 10
            else:
                attacker = None
        health_group.update(ticks, 50)

        if pygame.sprite.collide_rect_ratio(0.5)(player, health):
            player_health += 30
            if player_health > 100: player_health = 100
            health.X = random.randint(0, 700)
            health.Y = random.randint(0, 500)

        if player_health <= 0:
            game_over = True

        screen.fill((50, 50, 100))
        health_group.draw(screen)
        zombie_group.draw(screen)
        player_group.draw(screen)

        pygame.draw.rect(screen, (50, 150, 50, 180), Rect(300, 570, player_health * 2, 25))
        pygame.draw.rect(screen, (100, 200, 100, 180), Rect(300, 570, 200, 2))

        if game_over:
            print_text(font, 300, 100, "G A M E O V E R")


        pygame.display.update()