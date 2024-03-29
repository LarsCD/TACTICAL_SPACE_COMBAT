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
        self.module_level: int = name['module_level']

        # hp stats
        self.hp_max: int = stats['hp_max']
        self.current_hp: int = 0
        self.hp_percentage: float = 0

        # resistance stats
        self.resist_ammo_type: list = stats['resist_ammo_type']
        self.resist_damage_type: list = stats['resist_damage_type']
        self.resist_ammo_multiplier: float = stats['resist_ammo_multiplier']
        self.resist_damage_multiplier: float = stats['resist_damage_multiplier']

        # power stats
        self.current_power: int = 0
        self.power_req: int = stats['power_req']
        self.power_percentage: float = 0
        self.operational_power_factor: float = stats['operational_power_factor']
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

    # DEBUG METHODS
    def get_full_ident(self) -> str:
        """
        Return full identification of the module, (type, class_name, tag). For debug purposes only.
        :return: full identification string
        """
        return f'{str(self.type).lower()}_{str(self.class_name).lower()}_{str(self.tag).lower()}'

    # UPDATE METHODS
    def update_hp_percentage(self, round_nr=1) -> None:
        self.hp_percentage = round(((self.current_hp / self.hp_max) / 100), round_nr)

    def update_power_req_percentage(self, round_nr=1) -> None:
        self.power_percentage = round(((self.current_power / self.power_req) / 100), round_nr)

    def update_is_powered(self) -> None:
        self.is_powered = bool(self.current_power >= self.power_req)

    def update_is_damaged(self) -> None:
        if self.current_hp != self.hp_max:
            self.is_damaged = True
        else:
            self.is_damaged = False

    def update_is_destroyed(self) -> None:
        if self.current_hp <= 0:
            self.is_destroyed = True
        else:
            self.is_destroyed = False

    def update_module(self) -> None:
        """
        Updates module stats, calls all update methods.
        :return:
        """
        self.update_is_powered()
        self.update_is_damaged()
        self.update_is_damaged()
        self.update_hp_percentage()
        self.update_power_req_percentage()

    # HP METHODS
    # TODO: Change 'target' to type Target (class instance)
    def damage(self, damage: int, damage_type: str, target: dict) -> None:
        """
        Updates hp params on module and displays hit message
        :param damage: gets subtracted off current_hp
        :param damage_type: only for display
        :param target: only for display
        :return: None
        """
        self.current_hp -= damage
        print(f'{self.get_full_ident()} got {damage} \'{damage_type}\' damage from \'{target["tag"]}\'')

        self.update_is_damaged()
        self.update_is_destroyed()

        return None

    def destroy(self) -> None:
        """
        Set module hp to 0: destroy module (duh)
        """
        self.current_hp = 0
        self.update_is_damaged()
        self.update_is_destroyed()

        return None

    def revive(self) -> None:
        """
        Set module hp to hp_max
        """
        self.current_hp = self.hp_max
        self.update_is_damaged()
        self.update_is_destroyed()
        return None
