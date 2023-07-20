from game.components.power_ups.power_up import PowerUp
from game.utils.constants import HEART

class Heart(PowerUp):
    def __init__(self):
        self.image = HEART
        super().__init__(self.image)