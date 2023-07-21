import pygame

from game.components.bullets.bullet import Bullet
from game.utils.constants import POW, SCREEN_HEIGHT, SCREEN_WIDTH

class PowExplosion(Bullet):

    WIDTH = SCREEN_WIDTH
    HEIGHT = SCREEN_HEIGHT
    SPEED = 10

    def __init__(self, center):
        self.image = POW
        self.image = pygame.transform.scale(self.image,(self.WIDTH, self. HEIGHT))
        self.is_alive = True
        super().__init__(self.image, center)
        self.damage = 5

    def update(self, enemy):
        super().update(enemy)