import tkinter as tk
from tkinter import ttk


class SpaceShip:
    def __init__(self, name, module, body):
        self.name = name['name']
        self.tag = name['tag']
        self.type = name['type']
        self.class_name = name['class_name']

        # MODULES
        self.drives = module['drives']
        self.reactors = module['reactors']
        self.shields = module['shields']
        self.armor = module['armor']
        self.hull = module['hull']
        self.weapons = module['weapons']
        self.countermeasures = module['countermeasures']
        self.magazine = module['magazine']
        self.control = module['control']
        self.thrusters = module['thrusters']
        self.sensors = module['sensors']

        # BODY
        self.size = body['size']
        self.signature = body['signature']

        # STATUS FLAGS
        self.is_destroyed = False
        self.is_damaged = False

        # TARGET
        self.current_target = None


class SpaceGameUI:
    def __init__(self, master, player_ship, enemy_ship):
        self.master = master
        self.master.title("Space Battleship Game")

        # Initialize player and enemy ships
        self.player_ship = player_ship
        self.enemy_ship = enemy_ship

        # Create and place widgets
        self.create_widgets()

    def create_widgets(self):
        # Create a frame for player and enemy status
        status_frame = ttk.Frame(self.master)
        status_frame.pack(side=tk.TOP, padx=10, pady=10)

        # Player Ship Status
        player_status_frame = ttk.Frame(status_frame)
        player_status_frame.pack(side=tk.LEFT, padx=10)

        player_label = ttk.Label(player_status_frame, text="Player Ship Status")
        player_label.pack()

        self.display_ship_attributes(self.player_ship, player_status_frame)

        player_health_frame = ttk.Frame(player_status_frame)
        player_health_frame.pack()

        player_health_label = ttk.Label(player_health_frame, text="Health:")
        player_health_label.pack(side=tk.LEFT)

        self.player_health_bar = ttk.Progressbar(player_health_frame, orient=tk.HORIZONTAL, length=100,
                                                 mode="determinate",
                                                 maximum=self.player_ship.hull, value=self.player_ship.hull)
        self.player_health_bar.pack(side=tk.LEFT)

        # Enemy Ship Status
        enemy_status_frame = ttk.Frame(status_frame)
        enemy_status_frame.pack(side=tk.RIGHT, padx=10)

        enemy_label = ttk.Label(enemy_status_frame, text="Enemy Ship Status")
        enemy_label.pack()

        self.display_ship_attributes(self.enemy_ship, enemy_status_frame)

        enemy_health_frame = ttk.Frame(enemy_status_frame)
        enemy_health_frame.pack()

        enemy_health_label = ttk.Label(enemy_health_frame, text="Health:")
        enemy_health_label.pack(side=tk.LEFT)

        self.enemy_health_bar = ttk.Progressbar(enemy_health_frame, orient=tk.HORIZONTAL, length=50, mode="determinate",
                                                maximum=self.enemy_ship.hull, value=self.enemy_ship.hull)
        self.enemy_health_bar.pack(side=tk.LEFT)

        # Create buttons for player actions
        action_frame = ttk.Frame(self.master)
        action_frame.pack(side=tk.BOTTOM, pady=10)

        self.attack_button = ttk.Button(action_frame, text="Attack", command=self.attack)
        self.attack_button.pack(side=tk.LEFT)

        self.defend_button = ttk.Button(action_frame, text="Defend", command=self.defend)
        self.defend_button.pack(side=tk.LEFT)

        self.end_turn_button = ttk.Button(action_frame, text="End Turn", command=self.end_turn)
        self.end_turn_button.pack(side=tk.LEFT)

    def display_ship_attributes(self, ship, parent_frame):
        attributes_frame = ttk.Frame(parent_frame)
        attributes_frame.pack()

        attribute_labels = [
            'Name', 'Type', 'Class', 'Drives', 'Reactors', 'Shields', 'Armor',
            'Hull', 'Weapons', 'Countermeasures', 'Magazine', 'Control', 'Thrusters',
            'Sensors', 'Size', 'Signature'
        ]

        for label_text in attribute_labels:
            label = ttk.Label(attributes_frame, text=f"{label_text}:")
            label.grid(column=0, row=attribute_labels.index(label_text), sticky=tk.W, padx=5)

            value = getattr(ship, label_text.lower(), 'N/A')
            value_label = ttk.Label(attributes_frame, text=str(value))
            value_label.grid(column=1, row=attribute_labels.index(label_text), sticky=tk.W, padx=5)

    def update_health_bars(self):
        self.player_health_bar['value'] = self.player_ship.hull
        self.enemy_health_bar['value'] = self.enemy_ship.hull

    def attack(self):
        # Implement attack logic
        self.enemy_ship.hull -= 10  # Simulating damage
        self.update_health_bars()
        print("Attack!")

    def defend(self):
        # Implement defend logic
        self.player_ship.hull -= 5  # Simulating damage
        self.update_health_bars()
        print("Defend!")

    def end_turn(self):
        # Implement end turn logic
        print("End Turn!")


if __name__ == "__main__":
    player_ship_data = {
        'name': {'name': 'USS Enterprise', 'tag': 'NCC-1701', 'type': 'Frigate', 'class_name': 'Explorer'},
        'module': {
            'drives': 'Warp Drives',
            'reactors': 'Fusion Reactors',
            'shields': 'Energy Shields',
            'armor': 'Titanium Alloy',
            'hull': 100,
            'weapons': 'Phaser Cannons',
            'countermeasures': 'Deflector Shields',
            'magazine': 'Photon Torpedoes',
            'control': 'Ship Computer',
            'thrusters': 'Maneuvering Thrusters',
            'sensors': 'Advanced Sensors'
        },
        'body': {'size': 'Medium', 'signature': 'Low'}
    }

    enemy_ship_data = {
        'name': {'name': 'Imperial Destroyer', 'tag': 'ISD-001', 'type': 'Destroyer', 'class_name': 'Imperial'},
        'module': {
            'drives': 'Hyperdrives',
            'reactors': 'Antimatter Reactors',
            'shields': 'Particle Shields',
            'armor': 'Durasteel Plating',
            'hull': 50,
            'weapons': 'Turbo Laser Batteries',
            'countermeasures': 'Deflector Shields',
            'magazine': 'Ion Cannons',
            'control': 'Imperial AI',
            'thrusters': 'Ion Thrusters',
            'sensors': 'Imperial Sensors'
        },
        'body': {'size': 'Large', 'signature': 'High'}
    }

    root = tk.Tk()
    game_ui = SpaceGameUI(root, SpaceShip(**player_ship_data), SpaceShip(**enemy_ship_data))
    root.mainloop()
