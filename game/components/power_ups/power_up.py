import pygame, random
from game.utils.constants import SCREEN_WIDTH

class PowerUp:
    WIDTH = 30
    HEIGHT = 30
    POS_Y = 0
    SPEED = 5

    def __init__(self, image):
        self.image = image
        self.image = pygame.transform.scale(self.image,(self.WIDTH,self.HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(120, SCREEN_WIDTH-120)
        self.rect.y = self.POS_Y

    def update(self):
        self.rect.y += self.SPEED

    def draw(self, screen):
        screen.blit(self.image, self.rect)