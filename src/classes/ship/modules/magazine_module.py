from src.classes.ship.modules._module import Module
from src.classes.ship.ship_class import Ship


class Magazine(Module):
    def __init__(self, name: dict, stats: dict, Host_ship: Ship):
        super().__init__(name, stats, Host_ship)  # initialize params from Module class

        # ammo stats
        self.ammo_hold = stats['amount']
        self.ammo_type = stats['ammo_type']

        # SUPER OVERRIDE stats here
        super().requires_power = False
