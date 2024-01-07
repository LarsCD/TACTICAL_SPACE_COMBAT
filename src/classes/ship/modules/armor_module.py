from src.classes.ship.modules._module import Module


class Armor(Module):
    def __init__(self, name: dict, stats: dict):
        super().__init__(name, stats)  # initialize params from Module class

        # hit points
        self.shield_hp_max = stats['shield_hp_max']
        self.shield_hp_current = stats['shield_hp_current']

        # type
        self.armor_type = stats['armor_type']
