from src.classes.ship.modules._module import Module
from src.classes.ship.ship_class import Ship


class Shield(Module):
    def __init__(self, name: dict, stats: dict, Host_ship: Ship):
        super().__init__(name, stats, Host_ship)  # initialize params from Module class

        # hit points
        self.shield_hp_max = stats['shield_hp_max']
        self.shield_hp_current = stats['shield_hp_current']
        self.base_regen_rate = stats['base_regen_rate']
        self.current_regen_rate = 0

        # flags
        self.is_up = False

        # activation
        self.activation_time = stats['activation_time']

        # resistance
        self.resist_ammo_type = stats['resist_ammo_type']

        # call init methods
        self.update_current_regen_rate()

    def update_current_regen_rate(self):
        self.current_regen_rate = self.base_regen_rate * super().power_percentage
