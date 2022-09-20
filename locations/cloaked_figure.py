import time
from helpers.bcolors import bcolors
from location import Location


class CloakedFigureLocation(Location):

    def __init__(self):
        loc_name = "A Cloaked Figure"
        loc_options = ["give"]
        super().__init__(loc_name, loc_options=loc_options)

    def read_lore(self):
        print(
            f"{bcolors.WARNING}\"Hey kiddo... Mind getting me a beer? Bar cut me off...\"{bcolors.ENDC} the cloaked figure mumbles.")
        time.sleep(2)
        print(
            f"{bcolors.WARNING}\"I promise... I'll make it worth your while...\"{bcolors.ENDC}.")
        return
