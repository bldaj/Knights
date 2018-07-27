from os import path
import pickle

from utils import *
from battle import battle
from town import town_menu
from enemies import create_enemies_list
from character import Hero
from items.armor import tunic, light_boots

enemies = create_enemies_list()
hero = Hero()


def load_game():
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
        hero.stat_points = loaded_hero.stat_points
        hero.speed_attack = loaded_hero.speed_attack
        hero.inventory = loaded_hero.inventory

        with open('enemies.pickle', 'rb') as f2:
            global enemies
            enemies = pickle.load(f2)

        display_load_successful()
        return True
    else:
        print("You don't have save")
        return False


def tutorial():
    display_title('Tutorial')
    print('Tutorial text')

    if battle(hero=hero, enemies=enemies[0]):
        enemies.remove(enemies[0])
        hero.level_up()
    else:
        print('You managed to lose even during the tutorial...')
        exit()


def initialize_hero():
    hero.create_name()
    hero.health = 100
    hero.energy = 100
    hero.max_health = hero.health
    hero.max_energy = hero.energy
    hero.gold = 10
    hero.exp = 0
    hero.level = 1

    hero.set_breastplate(tunic)
    hero.set_boots(light_boots)


def new_game():
    print('STORY')
    initialize_hero()
    tutorial()


def main_menu():
    display_title('Main menu')

    commands = ['New game', 'Load game', 'Exit game']

    while True:
        display_commands(commands)
        cmd = get_cmd()

        if cmd == '1':
            new_game()
            break
        elif cmd == '2':
            if load_game():
                break
        elif cmd == '3':
            exit('Game exit')
        else:
            display_incorrect_command()


def start():
    main_menu()
    town_menu(hero=hero, enemies=enemies)


if __name__ == '__main__':
    start()
