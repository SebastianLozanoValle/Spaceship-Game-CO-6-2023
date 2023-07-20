import pygame

from game.components.planets.planet import Planet
from game.utils.constants import PLANET_1

class PurplePlanet(Planet):
    WIDTH = 80
    HEIGTH = 80

    def __init__ (self):
        self.image = PLANET_1
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGTH))
        super().__init__(self.image)