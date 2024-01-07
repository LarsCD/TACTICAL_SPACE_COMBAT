from src.classes.ship.modules._module import Module


class Magazine(Module):
    def __init__(self, name: dict, stats: dict):
        super().__init__(name, stats)  # initialize params from Module class

        # ammo stats
        self.ammo_hold = stats['amount']
        self.ammo_type = stats['ammo_type']

        # SUPER OVERRIDE stats here
        super().requires_power = False
