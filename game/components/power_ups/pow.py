from game.components.power_ups.power_up import PowerUp
from game.utils.constants import POW

class Pow(PowerUp):
    def __init__(self):
        self.image = POW
        super().__init__(self.image)