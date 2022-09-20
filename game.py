import imp
import time
from helpers.bcolors import bcolors
from helpers.print_helper import print_helper
from locations.tavern_main import TavernMainLocation
from inventory import Inventory
from player import Player


class Game:
    def __init__(self):
        self.current_location = None
        self.inventory = None
        self.player = None

    def intro_speech(self):
        player_name = self.player.get_name()
        print(
            f"Welcome, great hero {bcolors.BOLD}{player_name}!{bcolors.ENDC}")
        time.sleep(2)
        print(
            f"I'm thrilled that you're here. A great {bcolors.FAIL}evil {bcolors.ENDC}has plagued our world...")
        time.sleep(3)
        print(bcolors.UNDERLINE +
              f"You must save us, {bcolors.BOLD}{player_name}!{bcolors.ENDC} You're our only hope!")
        time.sleep(3)
    print_helper.add_space(50)

    def begin_game(self):
        print_helper.add_space(50)
        print(
            f"{bcolors.BOLD}{bcolors.OKGREEN}WELCOME TO {bcolors.FAIL}DRAGON QUEST!{bcolors.ENDC}")
        print_helper.add_space(1)
        player_name = input(
            f"{bcolors.BOLD}Enter your hero's name: {bcolors.ENDC}")
        print_helper.add_space(50)
        self.player = Player(player_name)
        self.current_location = TavernMainLocation()
        self.inventory = Inventory()
        if player_name != "test":
            self.intro_speech()
        self.game_loop()

    def run_lore_result(self, lore_result):
        if len(lore_result) == 2:
            # it's an item
            self.inventory.add_item(lore_result[0], lore_result[1])

    def move(self):
        adjacent = self.current_location.loc_adjacent
        if len(adjacent) == 0:
            print("there is nowhere to move to.")
            return
        item_idx = 0
        loc_dic = {}
        print("where would you like to move to?")
        for loc in adjacent:
            item_idx += 1
            loc_dic[item_idx] = loc
            print(f"{bcolors.OKCYAN}({item_idx}){bcolors.ENDC}: {loc.get_name()}")
        player_input = int(input(">> "))
        while (not player_input in loc_dic):
            print("this is not a valid location!")
            player_input = input(">> ")
        self.current_location = loc_dic[player_input]
        print_helper.add_space(50)
        print(f"{bcolors.OKGREEN}{self.current_location.get_name()}.{bcolors.ENDC}\n")

    def game_loop(self):
        for option in self.current_location.loc_options:
            first_letter = option[0]
            print(f"{bcolors.OKCYAN}({first_letter}){bcolors.ENDC}: {option}")
        player_selection = input(">> ")
        player_selection = player_selection.lower()

        if player_selection == ("m" or "move"):
            self.move()
        if player_selection == ("i" or "inventory"):
            self.inventory.list_items()
        if player_selection == ("c" or "check"):
            lore_result = self.current_location.read_lore()
            if lore_result != None:
                self.run_lore_result(lore_result)
        if player_selection == ("g" or "give"):
            print("fix this!")
        self.game_loop()  # yeah yeah recursion i know
