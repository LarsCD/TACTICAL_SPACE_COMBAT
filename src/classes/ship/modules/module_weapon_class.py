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
        self.hp_max = stats['hp_max']
        self.hp_current = stats['hp_current']
        self.hp_percentage = 0

        # ammo stats
        self.ammo_hold = stats['ammo_hold']
        self.ammo_type = stats['ammo_type']
        self.reload_time = stats['reload_time']

        # call init methods
        self.update_hp_percentage()

    def update_hp_percentage(self, round_nr=1):
        self.hp_percentage = round(((self.hp_current / self.hp_max) / 100), round_nr)
