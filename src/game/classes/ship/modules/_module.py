from src.game.classes.ship.ship_class import Ship


class Module:
    def __init__(self, name: dict, stats: dict, Host_ship: Ship):
        # this class servers as the common parameters for each module
        # name
        self.Host_ship: Ship = Host_ship
        self.name: str = name['name']
        self.tag: str = name['tag']
        self.type: str = name['type']
        self.class_name: str = name['class_name']

        # hp stats
        self.hp_max: int = stats['hp_max']
        self.hp_current: int = 0
        self.hp_percentage: float = 0

        # resistance stats
        self.resist_ammo_type: str = stats['resist_ammo_type']
        self.resist_damage_type: str = stats['resist_damage_type']
        self.resist_ammo_multiplier: float = stats['resist_ammo_multiplier']
        self.resist_damage_multiplier: float = stats['resist_damage_multiplier']

        # power stats
        self.power_current: int = 0
        self.power_req: int = stats['power_req']
        self.power_percentage: float = 0
        self.operational_power_factor: int = stats['operational_power_factor']
        self.power_req_threshold_factor: float = stats['power_req_threshold_factor']
        self.operational_power_threshold: float = 0

        # status flags
        self.requires_power: bool = True
        self.is_powered: bool = False
        self.is_destroyed: bool = False
        self.is_damaged: bool = False
        self.is_disabled: bool = False

        # call init methods
        self.revive()
        self.update_is_powered()
        self.update_is_damaged()
        self.update_is_damaged()
        self.update_hp_percentage()
        self.update_power_req_percentage()

    def get_full_ident(self) -> str:
        """
        Return full identification of the module, (type, class_name, tag). For debug purposes only.
        :return: full identification string
        """
        return f'{str(self.type).lower()}_{str(self.class_name).lower()}_{str(self.tag).lower()}'

    def update_hp_percentage(self, round_nr=1) -> None:
        self.hp_percentage = round(((self.hp_current / self.hp_max) / 100), round_nr)

    def update_power_req_percentage(self, round_nr=1) -> None:
        self.power_percentage = round(((self.power_current / self.power_req) / 100), round_nr)

    def update_is_powered(self) -> None:
        self.is_powered = bool(self.power_current >= self.power_req)

    def update_is_damaged(self) -> None:
        if self.hp_current != self.hp_max:
            self.is_damaged = True
        else:
            self.is_damaged = False

    def update_is_destroyed(self) -> None:
        if self.hp_current <= 0:
            self.is_destroyed = True
        else:
            self.is_destroyed = False

    # TODO: Change 'target' to type Target (class instance)
    def damage(self, damage: int, damage_type: str, target: dict) -> None:
        """
        Updates hp params on module and displays hit message
        :param damage: gets subtracted off hp_current
        :param damage_type: only for display
        :param target: only for display
        :return: None
        """
        self.hp_current -= damage
        self.update_is_damaged()
        self.update_is_destroyed()

        print(f'{self.get_full_ident()} got {damage} \'{damage_type}\' damage from \'{target["tag"]}\'')

        return None

    def destroy(self) -> None:
        """
        Set module hp to 0: destroy module (duh)
        """
        self.hp_current = 0
        self.update_is_damaged()
        self.update_is_destroyed()

        return None

    def revive(self) -> None:
        """
        Set module hp to hp_max
        """
        self.hp_current = self.hp_max
        self.update_is_damaged()
        self.update_is_destroyed()
        return None
