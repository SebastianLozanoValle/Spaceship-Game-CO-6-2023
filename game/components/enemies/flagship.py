import pygame
import numpy as np
from game.utils.constants import SCREEN_WIDTH, ENEMY_3, LEFT, RIGTH
from game.components.enemies.enemy import Enemy

class FlagShip(Enemy):
    WIDTH = 60
    HEIGHT = 80
    SPEED_X = 3
    
    INTERVAL = 1000
    SHOOTING_TIME = 60

    def __init__(self):
        self.image = ENEMY_3
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.lp = 5
        super().__init__(self.image)

    def move(self):
        self.rect.y = self.Y_POS
        if self.mov_x == LEFT:
            self.rect.x -= self.SPEED_X
            if self.index > self.INTERVAL or self.rect.x <= 0:
                self.mov_x = RIGTH
                self.index = 0
        else:
            self.rect.x += self.SPEED_X
            if self.index > self.INTERVAL or self.rect.x >= (SCREEN_WIDTH - self.rect.width):
                self.mov_x = LEFT
                self.index = 0

