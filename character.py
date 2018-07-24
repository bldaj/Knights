from levels import LEVELS
from utils import *


class Character:
    def __init__(self, name=None, health=None, energy=None, gold=None, exp=None, level=None):
        self.name = name
        self.health = health
        self.max_health = health
        self.max_energy = energy
        self.energy = energy
        self.gold = gold
        self.exp = exp
        self.level = level
        self.strength = 1
        self.agility = 1
        self.intelligence = 1
        self.physical_resistance = 1
        self.magical_resistance = 1
        self.stat_points = 1
        self.speed_attack = 1
        self.inventory = []

    def __repr__(self):
        return self.name


class Hero(Character):
    def __init__(self, name=None, health=None, energy=None, gold=None, exp=None, level=None):
        super().__init__(name=name, health=health, energy=energy, gold=gold, exp=exp, level=level)
        self.exp_multiplier = 1

    def create_name(self):
        while True:
            name = input('Enter hero name.\nName length must be less than 20 symbols: ')

            if len(name) != 0 and len(name) <= 20:
                self.name = name
                break
            else:
                print('Try again')

    def display_hero_infrormation(self):
        print('Name: {0} Level: {1}\n'
              'Health: {2}/{3} Experience: {4}\n'
              'Energy: {5}/{6} Gold: {7}\n'.format(self.name, self.level,
                                                   self.health, self.max_health, self.exp,
                                                   self.energy, self.max_energy, self.gold))

    def display_stats(self):
        print('Strength: {0}\n'
              'Agility: {1}\n'
              'Intelligence: {2}\n'
              'Speed attack: {3}\n'
              'Physical resistance: {4}\n'
              'Magical resistance: {5}'.format(self.strength, self.agility, self.intelligence, self.speed_attack,
                                               self.physical_resistance, self.magical_resistance))
        print('-' * 40)
        print('You have stat points: {0}'.format(self.stat_points))

    def level_up(self):
        for level, exp in enumerate(LEVELS):
            if self.exp > exp:
                continue
            elif self.exp <= exp:
                if self.level != level:
                    self._level_up(level)
                break
        else:
            self._level_up(level)

    def _level_up(self, level):
        self.stat_points += level - self.level

        self.level = level
        print('LEVEL UP\nYou got level {0}!'.format(self.level))

        self.max_health += 10 * level
        self.health = self.max_health
        self.max_energy += 10 * level
        self.energy = self.max_energy

    def increase_attributes(self):
        while True:
            self.display_stats()

            commands = ['Increase strength', 'Increase agility', 'Increase intelligence', 'Return back']
            display_commands(commands=commands)

            cmd = get_cmd()

            if cmd == '1':
                if self._is_enough_points():
                    self._increase_strength()
                else:
                    print("You don't have enough stat points")
            elif cmd == '2':
                if self._is_enough_points():
                    self._increase_agility()
                else:
                    print("You don't have enough action points")
            elif cmd == '3':
                if self._is_enough_points():
                    self._increase_intelligence()
                else:
                    print("You don't have enough action points")
            elif cmd == '4':
                return
            else:
                display_incorrect_command()

    def _is_enough_points(self):
        if self.stat_points > 0:
            return True
        else:
            return False

    def _increase_strength(self):
        self.strength += 1
        self.max_health += 2
        self.health += 2
        self.physical_resistance = round(0.1 + self.physical_resistance, 3)
        self.stat_points -= 1

    def _increase_agility(self):
        self.agility += 1
        self.speed_attack = round(0.1 + self.speed_attack, 3)
        self.stat_points -= 1

    def _increase_intelligence(self):
        self.intelligence += 1
        self.magical_resistance = round(0.1 + self.magical_resistance, 3)
        self.stat_points -= 1

    def display_inventory(self):
        for i, item in enumerate(self.inventory):
            print("%d: %s" % (i+1, item.name))
