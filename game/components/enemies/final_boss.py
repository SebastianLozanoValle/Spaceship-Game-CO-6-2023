import pygame, random
import numpy as np
from game.utils.constants import SCREEN_WIDTH, ENEMY_4, LEFT, RIGTH, BULLET_ENEMY_TYPE
from game.components.enemies.enemy import Enemy

class FinalBoss(Enemy):
    WIDTH = 500
    HEIGHT = 700
    SPEED_X = 1
    Y_POS = 0 - HEIGHT//2
    INTERVAL = 1000
    MOV_X = [LEFT,RIGTH]
    INTERVAL = SCREEN_WIDTH
    SHOOTING_TIME = 15
    SHOOTING_TIME_TWO = 12

    def __init__(self):
        self.image = ENEMY_4
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.lp = 100
        self.mov_x = random.choice(self.MOV_X)
        self.index = 0
        self.Y_POS
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

    def shoot(self, bullet_handler):
        if self.shooting_time % self.SHOOTING_TIME_TWO == 0:
            bullet_handler.add_bullet(BULLET_ENEMY_TYPE, self.rect.center)
        if self.shooting_time % self.SHOOTING_TIME == 0:
            bullet_handler.add_bullet(BULLET_ENEMY_TYPE, (self.rect.x+(self.WIDTH//8),self.rect.y + ((self.HEIGHT//4)*3)))
            bullet_handler.add_bullet(BULLET_ENEMY_TYPE, (self.rect.x+((self.WIDTH//8)*7),self.rect.y + ((self.HEIGHT//4)*3)))