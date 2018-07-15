from levels import LEVELS
from character import Character


class Enemy(Character):
    def check_level(self):
        for level, exp in enumerate(LEVELS):
            if self.exp > exp:
                continue
            elif self.exp <= exp:
                self.level = level
                self.stat_points += level
                break

    def set_strength(self, value):
        if value > 0:
            if value > self.stat_points:
                value = self.stat_points

            self.stat_points -= 1 * value

        self.strength += 1 * value
        self.max_health += 2 * value
        self.health += 2 * value
        self.physical_resistance += 1 * value

    def set_agility(self, value):
        if value > 0:
            if value > self.stat_points:
                value = self.stat_points

            self.stat_points -= 1 * value

        self.agility += 1 * value
        self.speed_attack += round(0.1 * value, 3)

    def set_intelligence(self, value):
        if value > 0:
            if value > self.stat_points:
                value = self.stat_points

            self.stat_points -= 1 * value

        self.intelligence += 1 * value
        self.magical_resistance += 1 * value


def create_enemies_list():
    enemies = []

    dummy = Enemy(
        name='Dummy',
        health=60,
        energy=100,
        gold=5,
        exp=60,
    )
    dummy.check_level()
    dummy.set_strength(-10)

    villager = Enemy(
        name='Villager',
        health=80,
        energy=100,
        gold=10,
        exp=100
    )
    villager.check_level()
    villager.set_agility(1)
    villager.set_strength(1)

    farmer = Enemy(
        name='Farmer',
        health=100,
        energy=100,
        gold=10,
        exp=120
    )
    farmer.check_level()
    farmer.set_strength(2)
    farmer.set_agility(1)

    knight = Enemy(
        name='Knight',
        health=140,
        energy=120,
        gold=15,
        exp=310
    )
    knight.check_level()
    knight.set_strength(10)

    enemies.extend((dummy, villager, farmer, knight))

    return enemies


create_enemies_list()