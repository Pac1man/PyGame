import pygame
from Player import Player
from Platform import Platform, DieBlock, Coin
pygame.init()
SIZE = (640, 480)

window = pygame.display.set_mode(SIZE)
screen = pygame.Surface(SIZE)
background = pygame.image.load('images/w3.png').convert()
font = pygame.font.SysFont("Consolas", 40)
hero = Player(60, 60)
left = right = up = down = False
level = [
    '------------------------------------------------------------------------------',
    '-                                           @                                -',
    '-     @                                                           @          -',
    '----  --------------------------------------------------------------------   -',
    '-                                                                            -',
    '-@ *  * *  *              **                                                 -',
    '-----------------        ----                       @       @          -------',
    '-                                                  ----    ----              -',
    '-                -------        ---------                         ---        -',
    '-                           @           -                                    -',
    '-                          ----         --------------------------------------',
    '-       @                                                                  @ -',
    '-    ------------                                                          ---',
    '-                                                                            -',
    '-      @                                      @                            @ -',
    '-  ---------------                            ---                          - -',
    '-                                                                            -',
    '--  -----                                                            ---------',
    '-     -----                                             @                    -',
    '-- *    @       **                         @                                 -',
    '------------------------------------------------------------------------------']

sprite_group = pygame.sprite.Group()
sprite_group.add(hero)
platforms = []

x = y = score = 0

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
        if col == "@":
            cn = Coin(x, y)
            sprite_group.add(cn)
            platforms.append(cn)
        x += 40
    y += 40
    x = 0


class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = pygame.Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)


def camera_func(camera, target_rect):
    l = -target_rect.x + SIZE[0] / 2
    t = -target_rect.y + SIZE[1] / 2
    w, h = camera.width, camera.height

    l = min(0, l)
    l = max(-(camera.width - SIZE[0]), l)
    t = max(-(camera.height - SIZE[1]), t)
    t = min(0, t)

    return pygame.Rect(l, t, w, h)


total_level_width = len(level[0]) * 40
total_level_height = len(level) * 40
camera = Camera(camera_func, total_level_width, total_level_height)
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.init()
sound = pygame.mixer.Sound("music/Doom.ogg").play(-1)
timer = pygame.time.Clock()
start_ticks = pygame.time.get_ticks()

while True:
    seconds = (pygame.time.get_ticks() - start_ticks) / 1000
    if seconds > 90:
        break
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            break

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

    coins_amount = 0
    screen.fill((10, 120, 10))
    screen.blit(background, (0, 0))
    text = font.render("End: " + str(int(90 - seconds)), True, (0, 0, 0))
    screen.blit(text, (500, 40))
   # counter_coins = font.render(str("Score: " + str(1)), True, (0, 0, 0))
   # screen.blit(counter_coins, (350, 40))
    hero.update(left, right, up, down, platforms)
    camera.update(hero)
    for e in sprite_group:
        screen.blit(e.image, camera.apply(e))

    window.blit(screen, (0, 0))

    pygame.display.flip()
    timer.tick(60)
