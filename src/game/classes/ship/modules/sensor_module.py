from _module import Module
from src.game.classes.ship.ship_class import Ship


class Sensor(Module):
    def __init__(self, name: dict, stats: dict, Host_ship: Ship):
        super().__init__(name, stats, Host_ship)  # initialize params from Module class

        # specific stats
        self.targeting_range = stats['targeting_range']
        self.targeting_accuracy_modifier = stats['targeting_accuracy_modifier']

        # super overrides
