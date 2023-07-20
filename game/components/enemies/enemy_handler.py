import pygame
import random

from game.components.enemies.ship import Ship
from game.components.enemies.xwing import XWing
from game.components.enemies.flagship import FlagShip
from game.components.enemies.final_boss import FinalBoss

class EnemyHandler:
    ENEMY_TYPES = [Ship,FlagShip]
    def __init__(self, game):
        self.game = game
        self.enemies = []
        self.enemies_destroyed = 0
        self.num_ships = 0
        self.num_xwings = 0
        self.num_bosses = 0

    def update(self, bullet_handler):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(bullet_handler)
            if not enemy.is_visible or enemy.lp <= 0:
                self.remove_enemy(enemy)
            if enemy.lp <= 0:
                if isinstance(enemy, XWing):
                    self.enemies_destroyed += 5
                elif isinstance(enemy, FlagShip):
                    self.enemies_destroyed += 2
                elif isinstance(enemy, FinalBoss):
                    self.enemies_destroyed += 100
                else:
                    self.enemies_destroyed += 1

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)



    def add_enemy(self):
        if len(self.enemies) < 10:
            if self.num_ships < 9 and self.game.timer < 55:
                self.enemies.append(self.ENEMY_TYPES[random.randint(0, len(self.ENEMY_TYPES) - 1)]())
                self.num_ships += 1
            if self.game.timer > 10 and self.num_xwings < 1:
                self.enemies.append(XWing())
                self.num_xwings += 1
            if self.game.timer > 60 and self.num_bosses <1:
                self.enemies.append(FinalBoss())
                self.num_bosses +=1

    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)
        if isinstance(enemy, Ship):
            self.num_ships -= 1
        if isinstance(enemy, FlagShip):
            self.num_ships -= 1
        if isinstance(enemy, FinalBoss):
            self.num_bosses += 1

    def reset(self):
        self.enemies = []
        self.enemies_destroyed = 0
        self.num_ships = 0
        self.num_xwings = 0
        self.num_bosses = 0