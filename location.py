from helpers.print_helper import print_helper
from helpers.bcolors import bcolors


class Location:
    def __init__(self, loc_name, loc_enemy_types, loc_adjacent):
        self.loc_name = loc_name
        self.loc_enemy_types = loc_enemy_types
        self.loc_adjacent = loc_adjacent

    def get_name(self):
        return self.loc_name

    def get_enemy_types(self):
        return self.loc_enemy_types

    def read_lore(self):
        print(f"{bcolors.FAIL}this location's lore hasn't been written!")
        print(f"{bcolors.WARNING}please ensure {self.get_name()} has a lore generated!")
