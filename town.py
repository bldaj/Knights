from os import path
from random import randint

import pickle

from utils import *
from battle import battle
from doctor import doctor
from marketplace import marketplace
from tavern import tavern
from events import find_money, sacrifice_the_poor, hear_the_whisper


def walk_around(hero):
    cmd = randint(1, 3)

    if cmd == 1:
        find_money(hero)
    elif cmd == 2:
        sacrifice_the_poor(hero)
    elif cmd == 3:
        hear_the_whisper()


def choose_enemy(enemies: list):
    while True:
        print()
        print('Press Enter to resume')

        for i, enemy in enumerate(enemies):
            if isinstance(enemy, list):
                print('{0}: {1} (level {2})'.format(i + 1, enemy[0], enemy[1].level))
            else:
                print('{0}: {1} (level {2})'.format(i + 1, enemy.name, enemy.level))

        try:
            cmd = get_cmd()

            if cmd == '':
                return
            else:
                return enemies[int(cmd)-1]
        except ValueError:
            display_incorrect_command()
        except IndexError:
            display_incorrect_command()


def save_game(hero, enemies):
    with open('save.pickle', 'wb') as f:
        pickle.dump(hero, f)
    with open('enemies.pickle', 'wb') as f2:
        pickle.dump(enemies, f2)

    display_save_successful()


def load_game(hero, enemies: list):
    if path.exists('save.pickle') and path.exists('enemies.pickle'):
        with open('save.pickle', 'rb') as f:
            loaded_hero = pickle.load(f)

        hero.name = loaded_hero.name
        hero.health = loaded_hero.health
        hero.max_health = loaded_hero.max_health
        hero.energy = loaded_hero.energy
        hero.max_energy = loaded_hero.max_energy
        hero.gold = loaded_hero.gold
        hero.exp = loaded_hero.exp
        hero.level = loaded_hero.level
        hero.strength = loaded_hero.strength
        hero.agility = loaded_hero.agility
        hero.intelligence = loaded_hero.intelligence
        hero.physical_resistance = loaded_hero.physical_resistance
        hero.magical_resistance = loaded_hero.magical_resistance
        hero.stat_points = loaded_hero.attribute_points
        hero.speed_attack = loaded_hero.speed_attack
        hero.hp_regen = loaded_hero.hp_regen
        hero.energy_regen = loaded_hero.energy_regen
        hero.luck = loaded_hero.luck
        hero.inventory = loaded_hero.inventory
        hero.helmet = loaded_hero.helmet
        hero.breastplate = loaded_hero.breastplate
        hero.bracers = loaded_hero.bracers
        hero.boots = loaded_hero.boots

        with open('enemies.pickle', 'rb') as f2:
            enemies = pickle.load(f2)

        display_load_successful()

        return hero, enemies
    else:
        print("You don't have save")
        return hero, enemies


def main_menu(hero, enemies):
    display_title('Main menu')

    commands = ['Back to the previous menu', 'Load game', 'Save game', 'Exit game']

    display_commands(commands=commands)
    cmd = get_cmd()

    if cmd == '1':
        return hero, enemies
    elif cmd == '2':
        hero, enemies = load_game(hero=hero, enemies=enemies)
        return hero, enemies
    elif cmd == '3':
        save_game(hero=hero, enemies=enemies)
        return hero, enemies
    elif cmd == '4':
        exit('Game exit')
    else:
        display_incorrect_command()
        main_menu(hero=hero, enemies=enemies)


def town_menu(hero, enemies: list):
    commands = ['Menu', 'To the Arena', 'Character', 'Doctor', 'Marketplace', 'Tavern', 'Walk around']

    while True:
        display_title('Town')
        display_commands(commands=commands)

        cmd = get_cmd()

        if cmd == '1':
            hero, enemies = main_menu(hero=hero, enemies=enemies)
        elif cmd == '2':
            if hero.health <= 0:
                print("I see you're the brave warrior! But I can't pass you on the Arena. "
                      "Take a rest, heal yourself and come back later!")
            else:
                enemy = choose_enemy(enemies=enemies)

                if enemy is not None:
                    if battle(hero=hero, enemies=enemy):
                        enemies.remove(enemy)

                        hero.health = round(hero.health, 3)
                        hero.energy = round(hero.energy, 3)

                        hero.level_up()
                    else:
                        hero.health = 0
                        hero.energy = 0
        elif cmd == '3':
            while True:
                display_commands(["Show hero's information", "Set attribute points", "Back to the previous menu"])

                cmd = get_cmd()

                if cmd == '1':
                    display_title("Hero's info")
                    hero.display_summary_information()
                elif cmd == '2':
                    hero.increase_attributes()
                elif cmd == '3':
                    break
                else:
                    display_incorrect_command()

        elif cmd == '4':
            doctor(hero=hero)
        elif cmd == '5':
            marketplace()
        elif cmd == '6':
            tavern(hero)
        elif cmd == '7':
            walk_around(hero)
        else:
            display_incorrect_command()
