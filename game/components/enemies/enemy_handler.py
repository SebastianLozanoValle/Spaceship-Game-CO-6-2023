from game.components.enemies.ship import Ship
from game.components.enemies.xwing import XWing

class EnemyHandler:
    def __init__(self):
        self.enemies = []

    def update(self):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update()
            if not enemy.is_visible:
                self.remove_enemy(enemy)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        if len(self.enemies) <= 2:
            self.enemies.append(Ship())
            self.enemies.append(XWing())

    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)