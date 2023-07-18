import pygame

from game.components.bullets.bullet import Bullet
from game.utils.constants import BULLET

class BulletPlayer(Bullet):

    WIDTH = 9
    HEIGHT = 32
    SPEED = 20

    def __init__(self, center):
        self.image = BULLET
        self.image = pygame.transform.scale(self.image,(self.WIDTH, self. HEIGHT))
        self.is_alive = True
        super().__init__(self.image, center)

    def update(self, enemy):
        self.rect.y -= self.SPEED
        super().update(enemy)