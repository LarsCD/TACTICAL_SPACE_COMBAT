
class Module_Magazine:
    def __init__(self, name: dict, stats: dict):
        # name
        self.name = name['name']
        self.tag = name['tag']
        self.weapon_type = name['weapon_type']
        self.class_name = name['class_name']

        # stats
        self.ammo_hold = stats['amount']
        self.ammo_type = stats['ammo_type']
