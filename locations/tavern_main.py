import time
from helpers.print_helper import print_helper
from helpers.bcolors import bcolors
from location import Location
from locations.bartender import BartenderLocation
from locations.cloaked_figure import CloakedFigureLocation


class TavernMainLocation(Location):

    def __init__(self):
        loc_name = "The Tavern Bar"
        loc_enemy_types = []
        loc_adjacent = []
        super().__init__(None, loc_name, loc_enemy_types, loc_adjacent)

        self.add_adjacent(BartenderLocation(self))
        self.add_adjacent(CloakedFigureLocation(self))

    def read_lore(self):
        print("You're in a worn down tavern, on the outskirts of town.")
        time.sleep(2)
        print(
            "Your boots stick to the floorboard below you, the smell of booze in the air.")
        time.sleep(2)
        print(f"There's a {bcolors.OKBLUE}Bartender{bcolors.ENDC} polishing a glass, and a {bcolors.WARNING}Cloaked Figure{bcolors.ENDC} in the corner.")
