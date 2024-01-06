from src.classes.ship.modules.module_class import Module


class Reactor(Module):
    def __init__(self, name: dict, stats: dict):
        super().__init__(name, stats)  # initialize params from Module class

        # SPECIFIC stats here
        self.power_output = stats['power_output']

        # SUPER OVERRIDE stats here
        super().requires_power = False
        super().is_powered = True
