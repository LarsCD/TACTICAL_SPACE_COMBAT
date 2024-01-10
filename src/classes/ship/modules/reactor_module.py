from src.classes.ship.modules._module import Module
from src.classes.ship.ship_class import Ship


class Reactor(Module):
    def __init__(self, name: dict, stats: dict, Host_ship: Ship):
        super().__init__(name, stats, Host_ship)  # initialize params from Module class

        # SPECIFIC stats here
        self.power_output = stats['power_output']

        # SUPER OVERRIDE stats here
        super().requires_power = False
        super().is_powered = True
