import pygame
from Player import Player
from Platform import Platform, DieBlock


SIZE = (640, 480)

window = pygame.display.set_mode(SIZE)
screen = pygame.Surface(SIZE)
background = pygame.image.load('images/w3.png').convert()


hero = Player(60, 60)
left = right = up = down = False

level = [
    '---------------------',
    '-                   -',
    '-                   -',
    '-        -----      -',
    '-                   -',
    '----------          -',
    '-                   -',
    '-    ------------ ---',
    '-                   -',
    '-                   -',
    '-  ---------------- -',
    '-                   -',
    '--  -----   ---------',
    '-     -----         -',
    '-- *                -',
    '---------------------', ]

sprite_group = pygame.sprite.Group()
sprite_group.add(hero)
platforms = []

x = y = 0

for row in level:
    for col in row:
        if col == "-":
            pl = Platform(x, y)
            sprite_group.add(pl)
            platforms.append(pl)
        if col == "*":
            bd = DieBlock(x, y)
            sprite_group.add(bd)
            platforms.append(bd)
        x += 30
    y += 30
    x = 0

done = True
timer = pygame.time.Clock()
while done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                left = True
            if e.key == pygame.K_RIGHT:
                right = True
            if e.key == pygame.K_UP:
                up = True
            if e.key == pygame.K_DOWN:
                down = True

        if e.type == pygame.KEYUP:
            if e.key == pygame.K_LEFT:
                left = False
            if e.key == pygame.K_RIGHT:
                right = False
            if e.key == pygame.K_UP:
                up = False
            if e.key == pygame.K_DOWN:
                down = False

    screen.fill((10, 120, 10))
    screen.blit(background, (0, 0))

    hero.update(left, right, up, down, platforms)
    sprite_group.draw(screen)

    window.blit(screen, (0, 0))

    pygame.display.flip()
    timer.tick(60)