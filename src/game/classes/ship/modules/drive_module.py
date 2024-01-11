from src.game.classes.ship.modules._module import Module
from src.game.classes.ship.ship_class import Ship


class Drive(Module):
    def __init__(self, name: dict, stats: dict, Host_ship: Ship):
        super().__init__(name, stats, Host_ship)  # initialize params from Module class

        # SPECIFIC stats here
        self.jump_distance_max: float = stats['jump_distance_max']
        self.current_jump_distance: float = 0

        # SUPER OVERRIDE stats here
