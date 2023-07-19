import pygame
import random

from game.components.enemies.ship import Ship
from game.components.enemies.xwing import XWing
# from game.components.enemies

class EnemyHandler:
    def __init__(self, game):
        self.game = game
        self.enemies = []
        self.enemies_destroyed = 0
        self.num_ships = 0
        self.num_xwings = 0
        self.enemies_dic = {
            "0": Ship(),
            "1": Ship(),
            "2": Ship(),
            "3": Ship(),
            "4": Ship(),
            "5": Ship(),
        }

    def update(self, bullet_handler):
        self.add_enemy()
        for enemy in self.enemies:
            # if type(enemy) == BulletEnemy:
            enemy.update(bullet_handler)
            if not enemy.is_visible or not enemy.is_alive:
                self.remove_enemy(enemy)
            if not enemy.is_alive:
                self.enemies_destroyed += 1

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)



    def add_enemy(self):
        if len(self.enemies) < 5:
            if self.num_ships < 4:
                self.enemies.append(Ship())
                self.num_ships += 1
                # random_key = random.choice(list(self.enemies_dic.keys()))
                # self.enemies.append(self.enemies_dic[random_key])
                # self.num_ships += 1
            if self.num_xwings == 0 and self.game.timer >= 10:
                self.enemies.append(XWing())
                self.num_xwings += 1
        # if len(self.enemies) < 5:
        #     if self.num_ships < 4:  # Verificar si hay menos de 4 naves
        #         if self.num_ships == 0:
        #             self.enemies.extend([Ship() for _ in range(4)])  # Agregar 4 instancias de Ship
        #             self.num_ships += 4
        #     if self.num_xwings == 0 and self.game.timer >= 10:
        #         self.enemies.append(XWing())
        #         self.num_xwings += 1



    # def add_enemy(self):
    #     if len(self.enemies) < 5:
    #         if self. num_ships < 5:
    #             self.enemies.append(Ship())
    #             #self.enemies_dic[str(random.randint(0, (len(self.enemies_dic) - 1)))]
    #         if self.timer > 10:
    #             if self.num_xwings <= 0:
    #                 self.enemies.append(XWing())

    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)
        if isinstance(enemy, Ship):
            self.num_ships -= 1
        if isinstance(enemy, XWing):
            self.num_xwings = 1

    def reset(self):
        self.enemies = []
        self.enemies_destroyed = 0
        self.num_ships = 0
        self.num_xwings = 0