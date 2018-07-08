from levels import LEVELS
from character import Character


class Enemy(Character):
    def check_level(self):
        for level, exp in enumerate(LEVELS):
            if self.exp > exp:
                continue
            elif self.exp <= exp:
                self.level = level
                break


def create_enemies_list():
    enemies = []

    dummy = Enemy(name='Dummy', health=60, energy=100, gold=5, exp=60)
    dummy.check_level()

    villager = Enemy(name='Villager', health=80, energy=100, gold=10, exp=100)
    villager.check_level()

    farmer = Enemy(name='Farmer', health=100, energy=100, gold=10, exp=120)
    farmer.check_level()

    knight = Enemy(name='Knight', health=140, energy=120, gold=15, exp=210)
    knight.check_level()

    enemies.extend((dummy, villager, farmer, knight))

    return enemies
