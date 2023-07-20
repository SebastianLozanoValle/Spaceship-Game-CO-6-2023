from game.components.power_ups.shield import Shield

class PowerUpHandler:
    def __init__(self):
        self.power_ups = []

    def update(self):
        self.add_power_up()
        for power_up in self.power_ups:
            power_up.update()

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def add_power_up(self):
        self.power_ups.append(Shield())

    def remove_power_up(self, power_up):
        self.power_ups.remove(power_up)