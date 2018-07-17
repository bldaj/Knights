from utils import *
from constants import *
from random import choice
# TODO: move Hero class into own module
from character import Hero
from enemies import Enemy


def miss_chance(character):
    chance = character.agility
    print(chance)


# TODO: change according on character sequence
def return_enemy_context(enemy, context):
    enemy.name = context['name']
    enemy.health = context['health']
    enemy.energy = context['energy']
    enemy.gold = context['gold']
    enemy.exp = context['gold']


# TODO: change according on character sequence
def check_winner(hero_health, enemy_health):
    if hero_health <= 0:
        return 'enemy'
    elif enemy_health <= 0:
        return 'hero'


def display_enemy_choice(enemy_name, enemy_choice, damage):
    if isinstance(enemy_choice, str):
        print('{0} has hit you in {1}'.format(enemy_name, enemy_choice))
        print('You received {0} damage'.format(damage))


# TODO: change according on character sequence
def display_characters_stats(hero, enemy):
    print('{0}: {1} {4:>20}: {5}\n{2}: {3}\n'.format('Your health', hero.health, 'Your energy', hero.energy,
                                                     'Enemy health', enemy.health))


# TODO: change according on character sequence
def display_turn(turn, hero_name, enemy_name):
    if turn == 1:
        print('{0} begins'.format(hero_name))
    elif turn == 2:
        print('{0} begins'.format(enemy_name))


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


def display_versus(hero, enemy):
    is_many = is_many_enemy(enemy)

    if is_many:
        print('{0} VS {1}'.format(hero.name, enemy[0]))
    elif not is_many:
        print('{0} VS {1}'.format(hero.name, enemy.name))


def make_sequence(hero, enemy):
    characters = [hero]

    is_many = is_many_enemy(enemy)

    if is_many:
        characters += enemy[1:]
    elif not is_many:
        characters.append(enemy)

    n = len(characters)

    for i in range(0, n-1):
        for j in range(0, n-i-1):
            if characters[j].speed_attack < characters[j+1].speed_attack:
                characters[j], characters[j+1] = characters[j+1], characters[j]
            elif characters[j].speed_attack == characters[j+1].speed_attack:
                choice_ = choice([1, 2])

                if choice_ == 2:
                    characters[j], characters[j + 1] = characters[j + 1], characters[j]

    return characters


def is_hero(character):
    if isinstance(character, Hero):
        return True
    elif isinstance(character, Enemy):
        return False
    else:
        # TODO: create class with exit codes using Enum module
        exit()


def is_many_enemy(enemy):
    if isinstance(enemy, Enemy):
        return False
    elif isinstance(enemy, list):
        return True
    else:
        exit()


def battle(hero, enemy):
    display_title('Battle')
    display_versus(hero=hero, enemy=enemy)

    sequence = make_sequence(hero=hero, enemy=enemy)

    for character in sequence:
        if is_hero(character):
            # TODO: create function which will provide to decide which enemy will be attacked
            pass




    # display_turn(turn=turn, hero_name=hero.name, enemy_name=enemies.name)
    #
    # enemy_context = {'name': enemies.name, 'health': enemies.health,
    #                  'energy': enemies.energy, 'gold': enemies.gold,
    #                  'exp': enemies.exp}
    #
    # while True:
    #     display_characters_stats(hero=hero, enemy=enemies)
    #
    #     if turn == 1:
    #         hero_action(hero=hero, enemy=enemies)
    #         if check_winner(hero.health, enemies.health) == 'hero':
    #             display_title("You're a winner!")
    #             hero.exp += round(enemies.exp * hero.exp_multiplier)
    #             hero.gold += enemies.gold
    #             return True
    #
    #         turn = toggle_turn(turn)
    #     elif turn == 2:
    #         enemy_action(hero=hero, enemy=enemies)
    #         if check_winner(hero.health, enemies.health) == 'enemy':
    #             display_title("You lose!")
    #             return_enemy_context(enemies, enemy_context)
    #             hero.health = 0
    #             return False
    #
    #         turn = toggle_turn(turn)
    #     else:
    #         print('Incorrect turn')
