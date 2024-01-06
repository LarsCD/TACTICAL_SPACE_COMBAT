class Module:
    def __init__(self, name: dict, stats: dict):
        # this class servers as the common parameters for each module
        # name
        self.name = name['name']
        self.tag = name['tag']
        self.type = name['type']
        self.class_name = name['class_name']

        # hp stats
        self.hp_max = stats['hp_max']
        self.hp_current = stats['hp_current']
        self.hp_percentage = 0

        # power stats
        self.requires_power = True
        self.is_powered = False
        self.power_current = 0
        self.power_req = stats['power_req']
        self.power_percentage = 0
        self.operational_power_factor = stats['operational_power_factor']
        self.power_req_threshold_factor = stats['power_req_threshold_factor']
        self.operational_power_threshold = 0

        # status flags
        self.is_destroyed = False
        self.is_damaged = False
        self.is_disabled = False

        # call init methods
        self.update_is_powered()
        self.update_hp_percentage()
        self.update_power_req_percentage()

    def update_hp_percentage(self, round_nr=1):
        self.hp_percentage = round(((self.hp_current / self.hp_max) / 100), round_nr)

    def update_power_req_percentage(self, round_nr=1):
        self.power_percentage = round(((self.power_current / self.power_req) / 100), round_nr)

    def update_is_powered(self):
        self.is_powered = bool(self.power_current >= self.power_req)

    def get_full_ident(self):
        return f'{str(self.type).lower()}_{str(self.class_name).lower()}_{str(self.tag).lower()}'
