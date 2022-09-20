import time
from helpers.print_helper import print_helper
from helpers.bcolors import bcolors
from location import Location
from locations.bartender import BartenderLocation
from locations.cloaked_figure import CloakedFigureLocation


class TavernMainLocation(Location):

    def __init__(self):
        loc_name = "The Tavern Bar"
        super().__init__(loc_name)
        self.add_adjacent_locations()

    def read_lore(self):
        print("You're in a worn down tavern, on the outskirts of town.")
        time.sleep(2)
        print(
            "Your boots stick to the floorboard below you, the smell of booze in the air.")
        time.sleep(2)
        print(f"There's a {bcolors.OKBLUE}Bartender{bcolors.ENDC} polishing a glass, and a {bcolors.WARNING}Cloaked Figure{bcolors.ENDC} in the corner.")

    def add_adjacent_locations(self):
        bartender = BartenderLocation()
        self.add_adjacent(bartender)
        cloaked = CloakedFigureLocation()
        self.add_adjacent(cloaked)
