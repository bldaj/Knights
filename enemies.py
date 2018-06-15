class Enemy:
    def __init__(self, name, health, energy, gold, exp, level, max_health=None, max_energy=None):
        self.name = name
        self.health = health
        self.energy = energy
        self.gold = gold
        self.exp = exp
        self.level = level
        self.max_health = max_health
        self.max_energy = max_energy
        self.inventory = []


enemies = []

dummy = Enemy('Dummy', 60, 100, 10, 100, '1')
villager = Enemy('Villager', 80, 100, 20, 160, '2')
farmer = Enemy('Farmer', 100, 100, 30, 180, '2')
knight = Enemy('Knight', 140, 120, 50, 250, '3')

enemies.extend((dummy, villager, farmer, knight))
