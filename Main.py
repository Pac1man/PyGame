import pygame
from Player import Player
from Platform import Platform

SIZE = (640, 480)

window = pygame.display.set_mode(SIZE)
screen = pygame.Surface(SIZE)

hero = Player(60, 60)
left = right = up = False

level = [
    '----------------',
    '-              -',
    '-      --      -',
    '-              -',
    '-              -',
    '-   -------    -',
    '-              -',
    '-              -',
    '-     ----     -',
    '-              -',
    '-              -',
    '----------------', ]

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
        x += 40
    y += 40
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

        if e.type == pygame.KEYUP:
            if e.key == pygame.K_LEFT:
                left = False
            if e.key == pygame.K_RIGHT:
                right = False
            if e.key == pygame.K_UP:
                up = False

    screen.fill((10, 120, 10))

    hero.update(left, right, up, platforms)
    sprite_group.draw(screen)
    window.blit(screen,(0, 0))

    pygame.display.flip()
    timer.tick(60)