from src.game.classes.ship.modules._module import Module
from src.game.classes.ship.ship_class import Ship


class Reactor(Module):
    def __init__(self, name: dict, stats: dict, Host_ship: Ship):
        super().__init__(name, stats, Host_ship)  # initialize params from Module class

        # SPECIFIC stats here

        # SUPER OVERRIDE stats here
