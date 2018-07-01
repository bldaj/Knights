import pickle

from utils import *
from battle import battle


def choose_enemy(enemies: list):
    while True:
        for i, enemy in enumerate(enemies):
            print('{0}: {1}'.format(i + 1, enemy.name))

        try:
            cmd = get_cmd()
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


def load_game(hero, enemies: list):
    with open('save.pickle', 'rb') as f:
        loaded_hero = pickle.load(f)

    hero.name = loaded_hero.name
    hero.health = loaded_hero.health
    hero.energy = loaded_hero.energy
    hero.gold = loaded_hero.gold
    hero.exp = loaded_hero.exp
    hero.level = loaded_hero.level

    with open('enemies.pickle', 'rb') as f2:
        enemies = pickle.load(f2)

    return hero, enemies


def main_menu(hero, enemies):
    display_title('Main menu')

    commands = ['Resume', 'Load game', 'Save game', 'Exit game']

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
    display_title('Town')

    commands = ['Menu', 'To the Arena', 'Character', 'Doctor', 'Marketplace', 'Walk around']

    while True:
        display_commands(commands=commands)

        cmd = get_cmd()

        if cmd == '1':
            hero, enemies = main_menu(hero=hero, enemies=enemies)
        elif cmd == '2':
            enemy = choose_enemy(enemies=enemies)

            if battle(hero=hero, enemy=enemy):
                enemies.remove(enemy)
        elif cmd == '3':
            hero.display_stats()

            for e in enemies:
                print(e.name, e.health)