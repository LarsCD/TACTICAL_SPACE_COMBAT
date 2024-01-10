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

        # target
        self.current_target = None

    def display_ship(self):
        # BY CHATGPT
        # Display ship name and type
        print(f"\033[1;36m{self.name} - {self.type}\033[0m")

        # Display power modules
        print("\033[1;33mPower Modules:\033[0m")
        print(f"  Drives: {self.drives}, Reactors: {self.reactors}")

        # Display hit point modules
        print("\033[1;31mHit Point Modules:\033[0m")
        print(f"  Shields: {self.shields}, Armor: {self.armor}, Hull: {self.hull}")

        # Display combat modules
        print("\033[1;91mCombat Modules:\033[0m")
        print(f"  Weapons: {self.weapons}, Countermeasures: {self.countermeasures}, Magazine: {self.magazine}")

        # Display control modules
        print("\033[1;35mControl Modules:\033[0m")
        print(f"  Control: {self.control}, Thrusters: {self.thrusters}")

        # Display sensor modules
        print("\033[1;32mSensor Modules:\033[0m")
        print(f"  Sensors: {self.sensors}")

        # Display body
        print("\033[1;34mBody:\033[0m")
        print(f"  Size: {self.size}, Signature: {self.signature}")

        # Display status flags
        print("\033[1;37mStatus Flags:\033[0m")
        print(f"  Destroyed: {self.is_destroyed}, Damaged: {self.is_damaged}")

        # Display current target
        print("\033[1;94mCurrent Target:\033[0m")
        print(f"  {self.current_target}")


# Example usage:
ship_data = {
    'name': 'USS Enterprise',
    'tag': 'NCC-1701',
    'type': 'Starship',
    'class_name': 'Constitution',
}

module_data = {
    'drives': 'Warp Drive',
    'reactors': 'Fusion Reactor',
    'shields': 'Deflector Shields',
    'armor': 'Titanium Alloy',
    'hull': 'Durasteel',
    'weapons': 'Phasers',
    'countermeasures': 'Chaff Launchers',
    'magazine': 'Photon Torpedoes',
    'control': 'Main Computer',
    'thrusters': 'Ion Thrusters',
    'sensors': 'Long-Range Scanners',
}

body_data = {
    'size': 'Large',
    'signature': 'Low',
}

ship = Ship(ship_data, module_data, body_data)
ship.display_ship()
