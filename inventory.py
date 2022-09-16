from helpers.bcolors import bcolors


class Inventory:

    def __init__(self):
        self.inventory = {  # item : count

        }
        self.ui_length = 20

    def list_items(self):
        if (len(self.inventory) == 0):
            print("you're not carrying anything.")
        else:
            print(f"{bcolors.OKGREEN}inventory:{bcolors.ENDC}")
            print("|" + "-" * self.ui_length + "|")
            for item in self.inventory:
                space = (self.ui_length - len(item) -
                         len(str(self.inventory[item])) - 4) * " "
                print(f"| {item}{space}| {self.inventory[item]} |")
            print("|" + "-" * self.ui_length + "|")

    def add_item(self, new_item, count):
        # check if item exists
        if new_item in self.inventory:
            self.inventory[new_item] += count
        else:
            self.inventory[new_item] = count
        print(f"added {count} {new_item} to your inventory.")
