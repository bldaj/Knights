from levels import LEVELS
from utils import *


class Character:
    def __init__(self, name=None, health=None, energy=None, gold=None, exp=None, level=None):
        self.name = name
        self.health = health
        self.max_health = health
        self.energy = energy
        self.max_energy = energy
        self.gold = gold
        self.exp = exp
        self.level = level
        self.strength = 1
        self.agility = 1
        self.intelligence = 1
        self.physical_resistance = 1
        self.magical_resistance = 1
        self.attribute_points = 1
        self.speed_attack = 1
        self.hp_regen = 1
        self.energy_regen = 1
        self.luck = 1
        self.inventory = []
        self.helmet = None
        self.breastplate = None
        self.bracers = None
        self.boots = None
        self.shield = None
        self.is_block = False

    def block(self):
        self.is_block = True

    # TODO: make universal functions (set_strength, set_agility and set_intelligence) for Hero and Enemy

    # TODO: add decrease methods (decrease_strength and etc.)

    def increase_strength(self, value=1):
        self.strength += 1
        self.max_health += 2
        self.health += 2
        # TODO: if calculating result < 0 then round will round to 0 instead of negative number
        self.physical_resistance = round(0.1 + self.physical_resistance, 3)
        self.hp_regen = round(0.1 + self.hp_regen, 3)
        self.energy_regen = round(0.1 + self.energy_regen, 3)

    def increase_agility(self):
        self.agility += 1
        self.speed_attack = round(0.1 + self.speed_attack, 3)
        self.luck += 1

    def increase_intelligence(self):
        self.intelligence += 1
        self.magical_resistance = round(0.1 + self.magical_resistance, 3)

    def deduct_attribute_points(self, value=1):
        self.attribute_points -= value

    def health_regeneration(self):
        if self.health < self.max_health:
            self.health = round(self.health + self.hp_regen, 3)

    def energy_regeneration(self):
        if self.energy < self.max_energy:
            self.energy = round(self.energy + self.energy_regen, 3)

    def set_helmet(self, helmet):
        self.helmet = helmet

        if helmet.additional_effects:
            for effect in helmet.additional_effects:
                if 'strength' in effect :
                    self.increase_strength()
                elif 'agility' in effect:
                    self.increase_agility()
                elif 'intelligence' in effect:
                    self.increase_intelligence()
                elif 'property' in effect:
                    pass
                elif 'skill' in effect:
                    pass
                else:
                    pass

    def set_breastplate(self, breastplate):
        self.breastplate = breastplate

        if breastplate.additional_effects:
            for effect in breastplate.additional_effects:
                if effect == 'strength':
                    self.increase_strength()
                elif effect == 'agility':
                    self.increase_agility()
                elif effect == 'intelligence':
                    self.increase_intelligence()
                elif effect == 'property':
                    pass
                elif effect == 'skill':
                    pass
                else:
                    pass

    def set_bracers(self, bracers):
        self.bracers = bracers

    def set_boots(self, boots):
        self.boots = boots

    def set_shield(self, shield):
        self.shield = shield

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

    def display_summary_information(self):
        self.display_hero_information()
        self.display_equipment()
        self.display_attributes()

    def display_hero_information(self):
        print('Name: {0} Level: {1}\n'
              'Health: {2}/{3} Experience: {4}\n'
              'Energy: {5}/{6} Gold: {7}\n'.format(self.name, self.level,
                                                   self.health, self.max_health, self.exp,
                                                   self.energy, self.max_energy, self.gold))

    def display_equipment(self):
        helmet_name = self.helmet.name if self.helmet is not None else 'Not equipped'
        breastplate_name = self.breastplate.name if self.breastplate is not None else 'Not equipped'
        bracers_name = self.bracers.name if self.bracers is not None else 'Not equipped'
        boots_name = self.boots.name if self.boots is not None else 'Not equipped'
        shield_name = self.shield if self.shield is not None else 'Not equipped'

        helmet_durability = self.helmet.durability if self.helmet is not None else 0
        breastplate_durability = self.breastplate.durability if self.breastplate is not None else 0
        bracers_durability = self.bracers.durability if self.bracers is not None else 0
        boots_durability = self.boots.durability if self.boots is not None else 0
        shield_durability = self.shield.durability if self.shield is not None else 0

        helmet_max_durability = self.helmet.max_durability if self.helmet is not None else 0
        breastplate_max_durability = self.breastplate.max_durability if self.breastplate is not None else 0
        bracers_max_durability = self.bracers.max_durability if self.bracers is not None else 0
        boots_max_durability = self.boots.max_durability if self.boots is not None else 0
        shield_max_durability = self.shield.max_durability if self.shield is not None else 0

        print('Helmet: {0} ({1}/{2})\n'
              'Armor: {3} ({4}/{5})\n'
              'Bracers: {6} ({7}/{8})\n'
              'Boots: {9} ({10}/{11})\n'
              'Shield: {12} ({13}/{14})\n'.format(helmet_name, helmet_durability, helmet_max_durability,
                                                  breastplate_name, breastplate_durability, breastplate_max_durability,
                                                  bracers_name, bracers_durability, bracers_max_durability,
                                                  boots_name, boots_durability, boots_max_durability,
                                                  shield_name, shield_durability, shield_max_durability))

    def display_attributes(self):
        print('Strength: {0}\n'
              'Agility: {1}\n'
              'Intelligence: {2}\n'
              'Luck: {3}\n'
              'Speed attack: {4}\n'
              'Physical resistance: {5}\n'
              'Magical resistance: {6}\n'
              'Health regeneration: {7}\n'
              'Energy regeneration: {8}'.format(self.strength, self.agility, self.intelligence, self.luck,
                                                self.speed_attack, self.physical_resistance,
                                                self.magical_resistance, self.hp_regen, self.energy_regen))
        print('-' * 40)
        print('You have attribute points: {0}'.format(self.attribute_points))

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
        self.attribute_points += (level - self.level) * 2

        self.level = level
        print('LEVEL UP\nYou got level {0}!'.format(self.level))

        self.max_health += 10 * level
        self.health = self.max_health
        self.max_energy += 10 * level
        self.energy = self.max_energy

    def increase_attributes(self):
        while True:
            self.display_attributes()

            commands = ['Increase strength', 'Increase agility', 'Increase intelligence', 'Back to the previous menu']
            display_commands(commands=commands)

            cmd = get_cmd()

            if cmd == '1':
                if self._is_enough_points():
                    self.increase_strength()
                    self.deduct_attribute_points()
                else:
                    print("You don't have enough stat points")
            elif cmd == '2':
                if self._is_enough_points():
                    self.increase_agility()
                    self.deduct_attribute_points()
                else:
                    print("You don't have enough action points")
            elif cmd == '3':
                if self._is_enough_points():
                    self.increase_intelligence()
                    self.deduct_attribute_points()
                else:
                    print("You don't have enough action points")
            elif cmd == '4':
                return
            else:
                display_incorrect_command()

    def _is_enough_points(self):
        if self.attribute_points > 0:
            return True
        else:
            return False

    def display_inventory(self):
        for i, item in enumerate(self.inventory):
            print("%d: %s" % (i+1, item.name))
