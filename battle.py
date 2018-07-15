from utils import *
from constants import *
from random import choice


def miss_chance(character):
    chance = character.agility
    print(chance)


def return_enemy_context(enemy, context):
    enemy.name = context['name']
    enemy.health = context['health']
    enemy.energy = context['energy']
    enemy.gold = context['gold']
    enemy.exp = context['gold']


def check_winner(hero_health, enemy_health):
    if hero_health <= 0:
        return 'enemy'
    elif enemy_health <= 0:
        return 'hero'


def display_enemy_choice(enemy_name, enemy_choice, damage):
    if isinstance(enemy_choice, str):
        print('{0} has hit you in {1}'.format(enemy_name, enemy_choice))
        print('You received {0} damage'.format(damage))


def display_turn(turn, hero_name, enemy_name):
    if turn == 1:
        print('{0} begins'.format(hero_name))
    elif turn == 2:
        print('{0} begins'.format(enemy_name))


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


def set_turn(hero, enemy):
    if hero.speed_attack > enemy.speed_attack:
        return 1
    elif hero.speed_attack < enemy.speed_attack:
        return 2
    else:
        return choice([1, 2])


def enemy_action(hero, enemy):
    cmd = choice(['1', '2', '3'])

    if cmd == '1':
        enemy.energy -= 15
        head_damage = int(40 + enemy.strength * HEAD_DAMAGE_MODIFIER)

        hero.health -= head_damage

        display_enemy_choice(enemy.name, 'head', head_damage)
    elif cmd == '2':
        enemy.energy -= 10
        body_damage = int(30 + enemy.strength * BODY_DAMAGE_MODIFIER)

        hero.health -= body_damage

        display_enemy_choice(enemy.name, 'body', body_damage)
    elif cmd == '3':
        enemy.energy -= 10
        legs_damage = int(20 + enemy.strength * LEGS_DAMAGE_MODIFIER)

        hero.health -= legs_damage

        display_enemy_choice(enemy.name, 'legs', legs_damage)


def hero_action(hero, enemy):
    head_damage = int(40 + hero.strength * HEAD_DAMAGE_MODIFIER)
    body_damage = int(30 + hero.strength * BODY_DAMAGE_MODIFIER)
    legs_damage = int(20 + hero.strength * LEGS_DAMAGE_MODIFIER)

    commands = ['Attack the head ({0} dmg/15 energy)'.format(head_damage),
                'Attack the body ({0} dmg/10 energy)'.format(body_damage),
                'Attack the legs ({0} dmg/5 energy)'.format(legs_damage)]
    display_commands(commands)

    cmd = get_cmd()

    if cmd == '1':
        hero.energy -= 15
        enemy.health -= head_damage
    elif cmd == '2':
        hero.energy -= 10
        enemy.health -= body_damage
    elif cmd == '3':
        hero.energy -= 5
        enemy.health -= legs_damage
    # elif cmd == '4':
    #     pass
    else:
        display_incorrect_command()
        hero_action(hero=hero, enemy=enemy)


def battle(hero, enemy):
    display_title('Battle')
    print('{0} VS {1}'.format(hero.name, enemy.name))

    turn = set_turn(hero=hero, enemy=enemy)
    display_turn(turn=turn, hero_name=hero.name, enemy_name=enemy.name)

    enemy_context = {'name': enemy.name, 'health': enemy.health,
                     'energy': enemy.energy, 'gold': enemy.gold,
                     'exp': enemy.exp}

    while True:
        display_characters_stats(hero=hero, enemy=enemy)

        if turn == 1:
            hero_action(hero=hero, enemy=enemy)
            if check_winner(hero.health, enemy.health) == 'hero':
                display_title("You're a winner!")
                hero.exp += round(enemy.exp * hero.exp_multiplier)
                hero.gold += enemy.gold
                return True

            turn = toggle_turn(turn)
        elif turn == 2:
            enemy_action(hero=hero, enemy=enemy)
            if check_winner(hero.health, enemy.health) == 'enemy':
                display_title("You lose!")
                return_enemy_context(enemy, enemy_context)
                hero.health = 0
                return False

            turn = toggle_turn(turn)
        else:
            print('Incorrect turn')
