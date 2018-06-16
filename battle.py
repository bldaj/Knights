from utils import *
from random import choice


def display_enemy_choice(enemy_name, enemy_choice):
    if isinstance(enemy_choice, str):
        print('{} has hit you in {}'.format(enemy_name, enemy_choice))


def display_characters_stats(hero, enemy):
    print('{0}: {1} {4:>20}: {5}\n{2}: {3}\n'.format('Your health', hero.health, 'Your energy', hero.energy,
                                                     'Enemy health', enemy.health))


def toggle_turn(turn):
    if isinstance(turn, int):
        if turn == 1:
            return 2
        elif turn == 2:
            return 1
    else:
        print('Incorrect turn type')


def set_turn():
    return choice([1, 2])


def enemy_action(hero, enemy):
    cmd = choice(['1', '2', '3'])

    if cmd == '1':
        enemy.energy -= 15
        hero.health -= 40
        display_enemy_choice(enemy.name, 'head')
    elif cmd == '2':
        enemy.energy -= 10
        hero.health -= 30
        display_enemy_choice(enemy.name, 'body')
    elif cmd == '3':
        enemy.energy -= 10
        hero.health -= 20
        display_enemy_choice(enemy.name, 'legs')


def hero_action(hero, enemy):
    commands = ['Attack the head (40 dmg/15 energy)', 'Attack the body (30 dmg/10 energy)',
                'Attack the legs (20 dmg/10 energy)', 'Use item (5 energy)']
    display_commands(commands)

    cmd = get_cmd()

    if cmd == '1':
        hero.energy -= 15
        enemy.health -= 40
    elif cmd == '2':
        hero.energy -= 10
        enemy.health -= 30
    elif cmd == '3':
        hero.energy -= 10
        enemy.health -= 20
    elif cmd == '4':
        pass
    else:
        display_incorrect_command()


def battle(hero, enemy):
    display_title('Battle')
    print('{} VS {}'.format(hero.name, enemy.name))

    turn = set_turn()

    while True:
        display_characters_stats(hero=hero, enemy=enemy)

        if turn == 1:
            hero_action(hero=hero, enemy=enemy)
            turn = toggle_turn(turn)
        elif turn == 2:
            enemy_action(hero=hero, enemy=enemy)
            turn = toggle_turn(turn)
        else:
            print('Incorrect turn')
