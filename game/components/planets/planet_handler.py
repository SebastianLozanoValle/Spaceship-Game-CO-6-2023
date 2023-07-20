import random

from game.components.planets.purple_planet import PurplePlanet
from game.components.planets.burning_planet import BurningPlanet
from game.utils.constants import SCREEN_HEIGHT

class PlanetHandler:
    PLANET_TYPES = [PurplePlanet, BurningPlanet]

    def __init__(self):
        self.planets = []

    def update(self):
        self.add_planet()
        for planet in self.planets:
            planet.update()
            if planet.rect.y > SCREEN_HEIGHT:
                self.remove_planet(planet)

    def draw(self, screen):
        for planet in self.planets:
            planet.draw(screen)

    def add_planet(self):
        if len(self.planets) < 2:
            self.planets.append(self.PLANET_TYPES[random.randint(0, len(self.PLANET_TYPES) - 1)]())

    def remove_planet(self, planet):
        self.planets.remove(planet)

    def reset(self):
        self.planets = []