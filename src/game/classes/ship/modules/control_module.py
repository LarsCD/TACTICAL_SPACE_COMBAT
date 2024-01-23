from _module import Module
from src.game.classes.ship.ship_class import Ship


class Control(Module):
    def __init__(self, name: dict, stats: dict, Host_ship: Ship):
        super().__init__(name, stats, Host_ship)  # initialize params from Module class

        # specific stats
        self.targeting_accuracy = stats['targeting_accuracy']
        self.control_modifier = stats['control_modifier']

        # super overrides
