from levels import LEVELS


class Enemy:
    def __init__(self, name, health, energy, gold, exp):
        self.name = name
        self.health = health
        self.energy = energy
        self.gold = gold
        self.exp = exp
        self.level = self.check_level()
        self.max_health = self.health
        self.max_energy = self.energy
        self.inventory = []

    def check_level(self):
        for level, exp in enumerate(LEVELS):
            if self.exp > exp:
                continue
            elif self.exp <= exp:
                return level


def create_enemies_list():
    enemies = []

    dummy = Enemy(name='Dummy', health=60, energy=100, gold=5, exp=60)
    villager = Enemy(name='Villager', health=80, energy=100, gold=10, exp=100)
    farmer = Enemy(name='Farmer', health=100, energy=100, gold=10, exp=120)
    knight = Enemy(name='Knight', health=140, energy=120, gold=15, exp=210)

    enemies.extend((dummy, villager, farmer, knight))

    return enemies
