
class Module_Weapon:
    def __init__(self, name: dict, stats: dict):
        # name
        self.name = name['name']
        self.tag = name['tag']
        self.weapon_type = name['weapon_type']
        self.class_name = name['class_name']

        # damage stats
        self.damage = stats['damage']
        self.damage_type = stats['damage_type']

        # hp stats
        self.hp = stats['hp']

        # ammo stats
        self.ammo_hold = stats['ammo_hold']
        self.ammo_type = stats['ammo_type']
        self.reload_time = stats['reload_time']