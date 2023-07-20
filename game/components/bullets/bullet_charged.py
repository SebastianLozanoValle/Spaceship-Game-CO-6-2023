import pygame

from game.components.bullets.bullet import Bullet
from game.utils.constants import BULLET_CHARGED

class BulletCharged(Bullet):

    WIDTH = 180
    HEIGHT = 32
    SPEED = 10

    def __init__(self, center):
        self.image = BULLET_CHARGED
        self.image = pygame.transform.scale(self.image,(self.WIDTH, self. HEIGHT))
        self.is_alive = True
        super().__init__(self.image, center)
        self.damage = 5

    def update(self, enemy):
        self.rect.y -= self.SPEED
        super().update(enemy)