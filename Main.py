import pygame
from Player import Player

SIZE = (640, 480)

window = pygame.display.set_mode(SIZE)

screen = pygame.Surface(SIZE)


class Platform:
    def __init__(self):
        self.ing = pygame.image.load('images/icon.png')


def make_level(level, platform):
    x = 0
    y = 0
    for row in level:
        for col in row:
            if col == '-':
                screen.blit(platform.ing, (x, y))
            x += 40
        y += 40
        x = 0


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

pl = Platform()


hero = Player(55, 55)
left = right = False

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

        if e.type == pygame.KEYUP:
            if e.key == pygame.K_LEFT:
                left = False
            if e.key == pygame.K_RIGHT:
                right = False

    screen.fill((10, 120, 10))

    make_level(level, pl)

    hero.update(left, right)
    hero.draw(screen)

    window.blit(screen, (0, 0))

    pygame.display.flip()
    timer.tick(60)