import time
from helpers.bcolors import bcolors
from location import Location


class cloaked_figure_location(Location):

    def __init__(self, parent):
        loc_name = "A Cloaked Figure"
        loc_enemy_types = []
        loc_adjacent = []
        super().__init__(parent, loc_name, loc_enemy_types, loc_adjacent)

    def read_lore(self):
        print(
            f"{bcolors.WARNING}\"Hey kiddo... Mind getting me a beer? Bar cut me off...\"{bcolors.ENDC} the cloaked figure mumbles.")
        time.sleep(2)
        print(
            f"{bcolors.WARNING}\"I promise... I'll make it worth your while...\"{bcolors.ENDC}.")
        return
