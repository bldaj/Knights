import pickle
from utils import *


def save_game(hero):
    with open('save.pickle', 'wb') as f:
        pickle.dump(hero, f)


def load_game(hero):
    with open('save.pickle', 'rb') as f:
        loaded_hero = pickle.load(f)

    hero.name = loaded_hero.name
    hero.health = loaded_hero.health
    hero.energy = loaded_hero.energy
    hero.gold = loaded_hero.gold
    hero.exp = loaded_hero.exp
    hero.level = loaded_hero.level

    return hero


def main_menu(hero):
    display_title('Main menu')

    commands = ['Resume', 'Load game', 'Save game', 'Exit game']

    display_commands(commands)
    cmd = get_cmd()

    if cmd == '1':
        return
    elif cmd == '2':
        hero = load_game(hero)
        return hero
    elif cmd == '3':
        save_game(hero)
    elif cmd == '4':
        exit('Game exit')
    else:
        display_incorrect_command()
        main_menu(hero)


def town_menu(hero, enemies: list):
    display_title('Town')

    print(hero.name, hero.health)

    for e in enemies:
        print(e.name, e.health)

    commands = ['Main menu']

    while True:
        display_commands(commands)

        cmd = get_cmd()

        if cmd == '1':
            main_menu(hero)
