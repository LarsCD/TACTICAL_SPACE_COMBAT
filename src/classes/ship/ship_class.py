class Ship:
    def __init__(self, name: dict, module: dict, body: dict):
        # name
        self.name = name['name']
        self.tag = name['tag']
        self.type = name['type']
        self.class_name = name['class_name']

        # MODULES
        # power module
        self.drives = module['drives']
        self.reactors = module['reactors']

        # hit point module
        self.shields = module['shields']
        self.armor = module['armor']
        self.hull = module['hull']

        # combat module
        self.weapons = module['weapons']
        self.countermeasures = module['countermeasures']
        self.magazine = module['magazine']

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





















