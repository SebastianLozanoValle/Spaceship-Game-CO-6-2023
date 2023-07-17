import numpy as np
import pygame

from game.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH

from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_2

class XWing(Enemy):
    WIDTH = 40
    HEIGTH = 60

    def __init__ (self):
        self.image = ENEMY_2
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGTH))
        super().__init__(self.image)

    def move(self):
        #obtener el tiempo en segundos ya que el metodo los retorna en milisegundos, se usa ticks para facilitar la legibilidad del codigo yno tener que pasarle parametros a la funcion
        t = pygame.time.get_ticks() / 1000
        #modificar para cambiar el tamaño del movimiento de la nave
        r = 250 

        x = r * np.cos(t) * np.cos(t/2) + (SCREEN_WIDTH - self.rect.width) / 2
        y = r * np.sin(t) * np.cos(t/2) + (SCREEN_HEIGHT - self.rect.height) / 2

        self.rect.x = x
        self.rect.y = y