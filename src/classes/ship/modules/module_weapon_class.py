import random

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
        self.ready_to_fire = False

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

    def update_ready_to_fire(self, target: dict) -> None:
        """
        Updates weapon's ready_to_fire flag, checks power, ammo,
        range to target and if reloading
        :param target: module or other instance being targeted
        """
        # check if weapon powered
        self.update_is_powered()
        if not self.is_powered:
            print(f'\'{self.get_full_ident()}\'cannot fire: weapon not powered')
            self.ready_to_fire = False

        # check if weapon is empty
        self.update_is_empty()
        if self.is_empty:
            print(f'\'{self.get_full_ident()}\'cannot fire: weapon is empty')
            self.ready_to_fire = False

        # check if weapon in range of target
        self.update_is_in_range(target['distance_from_ship'])
        if not self.is_in_range:
            print(f'\'{self.get_full_ident()}\'cannot fire: target not in range')
            self.ready_to_fire = False

        # check if weapon is reloading
        if self.is_reloading:
            print(f'\'{self.get_full_ident()}\'cannot fire: weapon is reloading')
            self.ready_to_fire = False

        # weapon is ready to fire
        self.ready_to_fire = True

        return None

    def fire(self, target: dict) -> int | tuple[int | int, float | float, float | float]:
        """
        Fires weapon, initiates reload and returns: damage, crit_multiplier,
        resist_multiplier
        :param target: module or other instance being targeted
        """
        # check if weapon is ready to fire
        self.update_ready_to_fire(target)
        if not self.ready_to_fire:
            return 0

        # check if crit
        damage_is_crit = random.random() < self.crit_chance
        if damage_is_crit:
            crit_multiplier = self.crit_multiplier
        else:
            crit_multiplier = 1

        # check if resistant armor
        if self.damage_type in ['resist_ammo_type']:
            resist_multiplier = target['resist_multiplier']
        else:
            resist_multiplier = 1

        # calculate damage
        damage = int(self.base_damage * crit_multiplier * resist_multiplier)

        return damage, crit_multiplier, resist_multiplier
