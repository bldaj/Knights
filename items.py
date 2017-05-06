class Food():
    def __init__(self, name, description, cost, health):
        self.name = name
        self.description = description
        self.cost = cost
        self.health = health

    def show_description(self):
        print(self.description)

    def use(self, character):
        character.health += self.health
        print("You used a %s" % self.name)


class Potion():
    def __init__(self, name, description, value, cost):
        self.name = name
        self.description = description
        self.value = value
        self.cost = cost
        # Name of potion can be only 'Health potion' or 'Energy potion'


class Weapon():
    def __init__(self, name, description, damage, weapon_kind, weapon_type, requirement_level, cost):
        self.name = name
        self.description = description
        self.damage = damage
        self.weapon_kind = weapon_kind  # sword, dagger, mace and etc.
        self.weapon_type = weapon_type  # one-handed or two-handed
        self.requirement_level = requirement_level
        self.cost = cost


carrot = Food('Carrot', 'Crispy vegetable', 1, 3)

health_potion = Potion('Health potion', 'This potion is healing your health', 20, 5)
energy_potion = Potion('Energy potion', 'This potion is restoring your energy', 20, 5)

sword = Weapon('Simple sword', 'Sharps as your life', 30, 'sword', 'one-handed', '1', 15)


trader = [health_potion, energy_potion, sword, carrot]
