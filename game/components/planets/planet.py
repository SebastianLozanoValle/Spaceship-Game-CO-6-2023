import random
from game.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH

class Planet:
    Y_POS = 0
    SPEED = 2

    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(image.get_width(), SCREEN_WIDTH - image.get_width())
        self.rect.y = self.Y_POS

    def update(self):
        self.move()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self):
        self.rect.y += self.SPEED