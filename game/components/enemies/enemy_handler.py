import pygame

from game.components.enemies.ship import Ship
from game.components.enemies.xwing import XWing

class EnemyHandler:
    def __init__(self):
        self.enemies = []
        self.clock = pygame.time.Clock()
        self.timer = 0
        self.num_ships = 0
        self.num_xwings = 0

    def update(self):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update()
            if not enemy.is_visible:
                self.remove_enemy(enemy)

        self.timer += self.clock.get_time() / 1000

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        if len(self.enemies) <= 4:
            if self. num_ships <= 3:
                self.enemies.append(Ship())
            if self.timer > 10:
                if self.num_xwings <= 0:
                    self.enemies.append(XWing())

    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)

    def draw_timer(self, screen):
        font = pygame.font.Font(None, 36)
        #como su nombre lo dice renderiza la fuente previamente creada y el 2f indica que despues de los dos puntos siguen 2 numeros de punto flotante, el true es para suavisar el renderizado
        text = font.render("Tiempo transcurrido: {:.2f} segundos".format(self.timer), True, (255, 255, 255))
        screen.blit(text, (10, 10))
