import items
from levels import LEVELS
from utils import *


class Character:
    def __init__(self, name=None, health=None, energy=None, gold=None, exp=None, level=None):
        self.name = name
        self.health = health
        self.energy = energy
        self.gold = gold
        self.exp = exp
        self.level = level
        self.max_health = health
        self.max_energy = energy
        self.strength = 1
        self.agility = 1
        self.intelligence = 1
        self.speed_attack = 1
        self.inventory = []


class Hero(Character):
    def __init__(self, name=None, health=None, energy=None, gold=None, exp=None, level=None):
        super().__init__(name=name, health=health, energy=energy, gold=gold, exp=exp, level=level)
        self.action_points = 1

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
              'Speed attack: {3}'.format(self.strength, self.agility, self.intelligence, self.speed_attack))
        print('-' * 40)
        print('You have action points: {0}'.format(self.action_points))

    def level_up(self):
        for level, exp in enumerate(LEVELS):
            if self.exp > exp:
                continue
            elif self.exp <= exp:
                if self.level != level:
                    self.level = level
                    print('LEVEL UP\nYou got {0} level!'.format(self.level))

                    self.max_health += 10 * level
                    self.health = self.max_health
                    self.max_energy += 10 * level
                    self.energy = self.max_energy
                    self.action_points += 1
                break

    def enhance_attributes(self):
        while True:
            self.display_stats()

            commands = ['Resume', 'Up strength', 'Up agility', 'Up intelligence']
            display_commands(commands=commands)

            cmd = get_cmd()

            if cmd == '1':
                return
            elif cmd == '2':
                if self._is_enough_points():
                    self._set_strength()
                else:
                    print("You don't have enough action points")
            elif cmd == '3':
                if self._is_enough_points():
                    self._set_agility()
                else:
                    print("You don't have enough action points")
            elif cmd == '4':
                if self._is_enough_points():
                    self._set_intelligence()
                else:
                    print("You don't have enough action points")
            else:
                display_incorrect_command()

    def _is_enough_points(self):
        if self.action_points > 0:
            return True
        else:
            return False

    def _set_strength(self):
        self.strength += 1
        self.action_points -= 1

    def _set_agility(self):
        self.agility += 1
        self.action_points -= 1

    def _set_intelligence(self):
        self.intelligence += 1
        self.action_points -= 1

    def display_inventory(self):
        for i, item in enumerate(self.inventory):
            print("%d: %s" % (i+1, item.name))

    def use_item(self):
        items_ids = []

        while True:
            if len(self.inventory) == 0:
                print("\nYou don't have any items\n")
                return 'Empty inventory'
            else:
                for i, item in enumerate(self.inventory):
                    items_ids.append(str(i+1))
                    print("[%d]: %s" % (i+1, item.name))

                cmd = input('Choose item: ')

                if cmd in items_ids:
                    item = self.inventory.pop(int(cmd)-1)

                    if isinstance(item, items.Food):
                        item.use(self)
                        break
                    elif isinstance(item, items.Potion):
                        if item.name == 'Health potion':
                            self.health += item.value

                            if self.health > self.max_health:
                                self.health = self.max_health

                            print('\n%s has healed health' % self.name)
                            break
                        elif item.name == 'Energy potion':
                            self.energy += item.value

                            if self.energy > self.max_energy:
                                self.energy = self.max_energy

                            print('\n%s has restored energy' % self.name)
                            break
                else:
                    print('Incorrect command\n')
