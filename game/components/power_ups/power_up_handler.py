import random

from game.components.power_ups.shield import Shield
from game.components.power_ups.heart import Heart

class PowerUpHandler:
    POWERS_TYPES = [Shield, Heart]
    INTERVAL_TIME = [150,250]

    def __init__(self):
        self.power_ups = []
        self.interval = random.randint(self.INTERVAL_TIME[0], self.INTERVAL_TIME[1])
        self.interval_time = 0

    def update(self, player):
        self.interval_time += 1
        if self.interval_time % self.interval == 0:
            self.add_power_up()
            self.interval_time = 0
        for power_up in self.power_ups:
            power_up.update(player)
            if not power_up.is_visible:
                self.remove_power_up(power_up)
            if power_up.is_used:
                player.active_power_up(power_up)
                player.gain_lp(power_up)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def add_power_up(self):
        self.power_ups.append(self.POWERS_TYPES[random.randint(0, len(self.POWERS_TYPES) - 1)]())

    def remove_power_up(self, power_up):
        self.power_ups.remove(power_up)

    def reset(self):
        self.power_ups = []
        self.interval_time = 0