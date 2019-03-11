from pygame.sprite import Sprite
from pygame import Surface

MOVE_SPEED = 7
GRAVITY = 0.4


class Player(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = Surface((23, 32))
        self.image.fill((150, 150, 150))
        self.x = x
        self.y = y
        self.xvel = 0
        self.yvel = 0
        self.onGround = False

    def upadte(self, left, right):
        if left:
            self.xvel += -MOVE_SPEED
        if right:
            self.xvel += MOVE_SPEED
        if not self.onGround:
            self.yvel += self.yvel
        if not (left or right):
            self.yvel += GRAVITY

    def draw(self, surf):
        surf.blit(self.image, (self.x, self.y))