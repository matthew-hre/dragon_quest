class Player:
    def __init__(self, name):
        self.health = 100
        self.name = name
        self.damage = 15
        self.crit_chance = 10  # out of 100
        self.level = 1

    def get_name(self):
        return self.name
