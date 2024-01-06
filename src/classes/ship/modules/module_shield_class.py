from src.classes.ship.modules.module_class import Module


class Shield(Module):
    def __init__(self, name: dict, stats: dict):
        super().__init__(name, stats)  # initialize params from Module class

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
