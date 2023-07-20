import pygame

from game.components.planets.planet import Planet
from game.utils.constants import PLANET_2

class BurningPlanet(Planet):
    WIDTH = 60
    HEIGTH = 60

    def __init__ (self):
        self.image = PLANET_2
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGTH))
        super().__init__(self.image)