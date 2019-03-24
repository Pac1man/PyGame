from pygame.sprite import Sprite, collide_rect
from pygame import Surface
import pyganim
import Platform

MOVE_SPEED = 5
JUMP_POWER = 10
GRAVITY = 0.7
ANIMATION_DELAY = 1
ANIMATION_STAY = [("images/hero/icon.png", ANIMATION_DELAY)]
ANIMATION_RIGHT = ["images/hero/iconL.png"]
ANIMATION_LEFT = ["images/hero/icon.png"]


class Player(Sprite):

    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = Surface((30, 30))
        self.xvel = 0
        self.yvel = 0
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.onGround = False
        self.score = 0

        def make_boltAnim(anim_list, delay):
            boltAnim = []
            for anim in anim_list:
                boltAnim.append((anim, delay))
            Anim = pyganim.PygAnimation(boltAnim)
            return Anim

        self.image.set_colorkey((0, 0, 0))
        self.boltAnimStay = pyganim.PygAnimation(ANIMATION_STAY)
        self.boltAnimStay.play()

        self.boltAnimRight = make_boltAnim(ANIMATION_RIGHT, ANIMATION_DELAY)
        self.boltAnimRight.play()

        self.boltAnimLeft = make_boltAnim(ANIMATION_LEFT, ANIMATION_DELAY)
        self.boltAnimLeft.play()

    def update(self, left, right, up, down, platforms):

        if left:
            self.xvel = -MOVE_SPEED
            self.image.fill((0, 0, 0))
            self.boltAnimLeft.blit(self.image, (0, 0))

        if right:
            self.xvel = MOVE_SPEED
            self.image.fill((0, 0, 0))
            self.boltAnimRight.blit(self.image, (0, 0))

        if up:
            if self.onGround:
                self.yvel += GRAVITY
            self.yvel = -MOVE_SPEED + GRAVITY

        if not (left or right):
            self.xvel = 0

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
                    self.die()
                if isinstance(pl, Platform.Coin):
                    Platform.Coin.kill(pl)
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
        import pygame
        pygame.time.wait(50)
        self.teleporting(self.rect.x, self.rect.y)

    def teleporting(self, goX, goY):
        self.rect.x = goX
        self.rect.y = goY
