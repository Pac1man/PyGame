from pygame.sprite import Sprite
from pygame.image import load


class Platform(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = load("images/platform.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class DieBlock(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = load("images/portal2.png")


class Coin(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = load("images/Coin1.png")