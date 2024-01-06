from src.classes.ship.modules.module_class import Module


class Weapon(Module):
    def __init__(self, name: dict, stats: dict):
        super().__init__(name, stats)  # initialize params from Module class

        # damage stats
        self.base_damage = stats['base_damage']
        self.damage_type = stats['damage_type']
        self.crit_chance = stats['crit_chance']
        self.crit_multiplier = stats['crit_multiplier']

        # ammo stats
        self.ammo_hold = stats['ammo_hold']
        self.ammo_type = stats['ammo_type']
        self.current_ammo_left = 0
        self.current_ammo_left_percentage = 0
        self.ammo_usage_per_fire = stats['ammo_usage_per_fire']
        self.is_empty = True

        # weapon stats
        self.base_range = stats['base_range']
        self.is_in_range = False
        self.accuracy = stats['accuracy']
        self.reload_time = stats['reload_time']
        self.is_reloading = False

        # effects
        self.status_effects = stats['status_effects']

        # call init methods
        self.update_current_ammo_left_percentage()

    def update_current_ammo_left_percentage(self, round_nr=1):
        self.current_ammo_left_percentage = round(((self.current_ammo_left / self.ammo_hold) / 100), round_nr)

    def update_is_in_range(self, target_range):
        self.is_in_range = bool(target_range > self.base_range)

    def update_is_empty(self):
        if self.current_ammo_left <= 0:
            self.current_ammo_left = 0
            self.is_empty = True
        else:
            self.is_empty = False

    def check_if_ready_to_fire(self, target):
        # check weapon is if empty
        self.update_is_empty()
        if self.is_empty:
            print(f'\'{self.get_full_ident()}\'cannot fire: is empty')
            return 0

        # check if weapon in range of target
        self.update_is_in_range(target['distance_from_ship'])
        if not self.is_in_range:
            print(f'\'{self.get_full_ident()}\'cannot fire: target not in range')



    def fire(self, target: dict):

        # state: ship is in range and ready to fire
        pass


