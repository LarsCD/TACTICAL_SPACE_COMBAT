from _module import Module
from src.game.classes.ship.ship_class import Ship


class Thruster(Module):
    def __init__(self, name: dict, stats: dict, Host_ship: Ship):
        super().__init__(name, stats, Host_ship)  # initialize params from Module class

        # specific stats
        self.thrust_power = stats['thrust_power']
        self.control_modifier = stats['control_modifier']

        # super overrides
