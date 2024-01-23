class Ship:
    def __init__(self, name: dict, module: dict, body: dict):
        # name
        self.name = name['name']
        self.tag = name['tag']
        self.type = name['type']
        self.class_name = name['class_name']

        # MODULES
        # power module
        self.drives = module['drives']  # DATA
        self.reactors = module['reactors']  # DATA

        # hit point module
        self.shields = module['shields']  # DATA
        self.armor = module['armor']  # DATA
        self.hull = module['hull']  # DATA

        # combat module
        self.weapons = module['weapons']  # DATA
        self.magazine = module['magazine']  # DATA

        # control module
        self.control = module['control']
        self.thrusters = module['thrusters']

        # sensor modules
        self.sensors = module['sensors']

        # BODY
        self.size = body['size']
        self.signature = body['signature']

        # status flags
        self.is_destroyed = False
        self.is_damaged = False

        # target
        self.current_target = None
