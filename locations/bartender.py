import time
from helpers.bcolors import bcolors
from location import Location


class BartenderLocation(Location):

    def __init__(self):
        loc_name = "The Bartender"
        super().__init__(loc_name)
        print(self.loc_adjacent)

    def read_lore(self):
        print(
            f"{bcolors.OKBLUE}\"Look who finally woke up,\"{bcolors.ENDC} the bartender scoffs.")
        time.sleep(2)
        print(f"\"Ugh... at least I had a good nap.\"")
        time.sleep(2)
        print(
            f"{bcolors.OKBLUE}\"Here, take this. It'll wake you right up.\"{bcolors.ENDC}")
        time.sleep(1)
        return ["beer", 1]
