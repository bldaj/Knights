from utils import *
from enemies import create_enemies_list
from character import Character


enemies = create_enemies_list()
hero = Character()


def save_game():
    pass


def load_game():
    pass


def initialize_hero():
    hero.create_name()
    hero.health = 100
    hero.energy = 100
    hero.gold = 10
    hero.exp = 0
    hero.level = 1


def new_game():
    hero.display_stats()
    initialize_hero()


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
