import pickle

from utils import *
from battle import battle
from town import town_menu
from enemies import create_enemies_list
from character import Hero

enemies = create_enemies_list()
hero = Hero()


def load_game():
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

    with open('enemies.pickle', 'rb') as f2:
        global enemies
        enemies = pickle.load(f2)


def tutorial():
    display_title('Tutorial')
    print('Tutorial text')

    if battle(hero=hero, enemy=enemies[0]):
        enemies.remove(enemies[0])
        hero.level_up()
    else:
        print('You managed to lose even during the tutorial...')


def initialize_hero():
    hero.create_name()
    hero.health = 100
    hero.energy = 100
    hero.max_health = hero.health
    hero.max_energy = hero.energy
    hero.gold = 10
    hero.exp = 0
    hero.level = 0


def new_game():
    print('STORY')
    initialize_hero()
    tutorial()


def main_menu():
    display_title('Main menu')

    commands = ['New game', 'Load game', 'Exit game']

    display_commands(commands)
    cmd = get_cmd()

    if cmd == '1':
        new_game()
    elif cmd == '2':
        load_game()
    elif cmd == '3':
        exit('Game exit')
    else:
        display_incorrect_command()
        main_menu()


def start():
    main_menu()
    town_menu(hero=hero, enemies=enemies)


if __name__ == '__main__':
    start()
