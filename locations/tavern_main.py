import time
from helpers.print_helper import print_helper
from helpers.bcolors import bcolors
from location import Location
from locations.bartender import bartender_location


class tavern_main_location(Location):

    loc_name = "The Tavern Bar"
    loc_enemy_types = []
    loc_adjacent = [bartender_location()]

    def __init__(self):
        super().__init__(self.loc_name, self.loc_enemy_types, self.loc_adjacent)

    def read_lore(self):
        print("You're in a worn down tavern, on the outskirts of town.")
        time.sleep(2)
        print(
            "Your boots stick to the floorboard below you, the smell of booze in the air.")
        time.sleep(2)
        print(f"There's a {bcolors.OKBLUE}Bartender{bcolors.ENDC} polishing a glass, and a {bcolors.WARNING}Cloaked Figure{bcolors.ENDC} in the corner.")
