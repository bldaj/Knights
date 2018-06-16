import pickle

from utils import *
from battle import battle
from enemies import create_enemies_list
from character import Character

enemies = create_enemies_list()
hero = Character()


def save_game():
    with open('save.pickle', 'wb') as f:
        pickle.dump(hero, f)


def load_game():
    with open('save.pickle', 'rb') as f:
        loaded_hero = pickle.load(f)

    hero.name = loaded_hero.name
    hero.health = loaded_hero.health
    hero.energy = loaded_hero.energy
    hero.gold = loaded_hero.gold
    hero.exp = loaded_hero.exp
    hero.level = loaded_hero.level


def tutorial():
    display_title('Tutorial')
    print('tutor text')

    battle(hero=hero, enemy=enemies[0])


def initialize_hero():
    hero.create_name()
    hero.health = 100
    hero.energy = 100
    hero.gold = 10
    hero.exp = 0
    hero.level = 1


def new_game():
    print('STORY')
    initialize_hero()
    tutorial()


def main_menu():
    display_title('Main menu')

    commands = ['New game', 'Load game', 'Save game', 'Exit game']

    display_commands(commands)
    cmd = get_cmd()

    if cmd == '1':
        new_game()
    elif cmd == '2':
        load_game()
    elif cmd == '3':
        save_game()
    elif cmd == '4':
        exit('Game exit')
    else:
        display_incorrect_command()
        main_menu()


def start():
    main_menu()


if __name__ == '__main__':
    start()
