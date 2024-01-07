from src.classes.ship.modules._module import Module


class Reactor(Module):
    def __init__(self, name: dict, stats: dict):
        super().__init__(name, stats)  # initialize params from Module class

        # SPECIFIC stats here

        # SUPER OVERRIDE stats here
