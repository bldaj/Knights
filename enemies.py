from levels import LEVELS
from character import Character

from items.armor import *


class Enemy(Character):
    def check_level(self):
        for level, exp in enumerate(LEVELS):
            if self.exp > exp:
                continue
            elif self.exp <= exp:
                self.level = level
                self.attribute_points += level
                break
        else:
            self.level = level
            self.attribute_points += level

    def set_strength(self, value):
        if value > 0:
            if value > self.attribute_points:
                value = self.attribute_points

            self.attribute_points -= 1 * value
            # self.deduct_attribute_points(1*value)

        self.increase_strength(value=value)

        self.strength += 1 * value
        self.max_health += 2 * value
        self.health += 2 * value
        self.physical_resistance += 1 * value

    def set_agility(self, value):
        if value > 0:
            if value > self.attribute_points:
                value = self.attribute_points

            self.attribute_points -= 1 * value

        self.agility += 1 * value
        self.speed_attack += round(0.1 * value, 3)

    def set_intelligence(self, value):
        if value > 0:
            if value > self.attribute_points:
                value = self.attribute_points

            self.attribute_points -= 1 * value

        self.intelligence += 1 * value
        self.magical_resistance += 1 * value


def create_enemies_list():
    dummy = Enemy(
        name='Dummy',
        health=60,
        energy=100,
        gold=5,
        exp=60,
    )
    dummy.check_level()
    dummy.set_strength(-10)
    dummy.set_agility(-5)


    villager = Enemy(
        name='Villager',
        health=80,
        energy=100,
        gold=10,
        exp=100
    )
    villager.check_level()
    villager.set_strength(1)
    villager.set_breastplate(tunic)
    villager.set_boots(light_boots)


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
    farmer.set_helmet(leather_helmet)
    farmer.set_breastplate(tunic)
    farmer.set_boots(light_boots)


    regular_fighter = Enemy(
        name='Regular fighter',
        health=140,
        energy=120,
        gold=15,
        exp=410
    )
    regular_fighter.check_level()
    regular_fighter.set_strength(3)
    regular_fighter.set_agility(1)
    regular_fighter.set_breastplate(gambeson)
    regular_fighter.set_boots(light_boots)


    left_head_of_snake = Enemy(
        name='Left head of Snake',
        health=80,
        energy=100,
        gold=10,
        exp=410
    )
    left_head_of_snake.check_level()
    left_head_of_snake.set_agility(4)

    right_head_of_snake = Enemy(
        name='Right head of Snake',
        health=80,
        energy=100,
        gold=10,
        exp=410
    )
    right_head_of_snake.check_level()
    right_head_of_snake.set_agility(4)


    former_warrior = Enemy(
        name='Former warrior',
        health=150,
        energy=140,
        gold=20,
        exp=930
    )
    former_warrior.check_level()
    former_warrior.set_strength(4)
    former_warrior.set_agility(1)
    former_warrior.set_helmet(leather_helmet)
    former_warrior.set_breastplate(gambeson)
    former_warrior.set_bracers(leather_bracers)
    former_warrior.set_boots(leather_boots)

    return [dummy, villager, farmer, regular_fighter, ['Two-headed Snake', left_head_of_snake, right_head_of_snake],
            former_warrior]
