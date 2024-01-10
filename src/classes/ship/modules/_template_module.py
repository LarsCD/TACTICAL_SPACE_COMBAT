from _module import Module
from src.classes.ship.ship_class import Ship


class NAME(Module):
    def __init__(self, name: dict, stats: dict, Host_ship: Ship):
        super().__init__(name, stats, Host_ship)  # initialize params from Module class

        # specific stats

        # super overrides
