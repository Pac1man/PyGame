from pygame.sprite import Sprite, collide_rect
from pygame import Surface, time
import Platform

MOVE_SPEED = 7
JUMP_POWER = 10
GRAVITY = 0.0


class Player(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = Surface((23, 32))
        self.image.fill((150, 150, 150))
        self.xvel = 0
        self.yvel = 0
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.onGround = False

    def update(self, left, right, up, down, platforms):
        if left:
            self.xvel = -MOVE_SPEED
        if right:
            self.xvel = MOVE_SPEED
        if up:
            self.yvel = -MOVE_SPEED + GRAVITY
        if down:
            self.yvel = MOVE_SPEED

        if not (left or right):
            self.xvel = 0
        if not (down or up):
            self.yvel = 0

        if not self.onGround:
            self.yvel += GRAVITY

        if not self.onGround:
            self.yvel += GRAVITY

        self.onGround = False

        self.rect.x += self.xvel
        self.collide(self.xvel, 0, platforms)
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

    def collide(self, xvel, yvel, platforms):
        for pl in platforms:
            if collide_rect(self, pl):
                if isinstance(pl, Platform.DieBlock):  # если пересакаемый блок - blocks.BlockDie или Monster
                    self.die()  # умираем
                if xvel > 0:
                    self.rect.right = pl.rect.left
                if xvel < 0:
                    self.rect.left = pl.rect.right
                if yvel > 0:
                    self.rect.bottom = pl.rect.top
                    self.onGround = True
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = pl.rect.bottom
                    self.yvel = 0

    def die(self):
        time.wait(50000)
        self.teleporting(self.rect.x, self.rect.y)

    def teleporting(self, goX, goY):
        self.rect.x = goX
        self.rect.y = goY
