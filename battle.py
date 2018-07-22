from utils import *
from constants import *
from random import choice, randint
# TODO: move Hero class into own module
from character import Hero
from enemies import Enemy


def return_enemies_context(enemies, enemies_context):
    if isinstance(enemies, list):
        for enemy in enemies:
            for enemy_context in enemies_context:
                if enemy.name == enemy_context['name']:
                    enemy.health = enemy_context['health']
                    enemy.energy = enemy_context['energy']
    else:
        enemies.health = enemies_context[0]['health']
        enemies.energy = enemies_context[0]['energy']


def save_enemies_context(enemies) -> list:
    enemies_context = []

    if is_many_enemies(enemies):
        for enemy in enemies:
            enemy_context = {
                'name': enemy.name,
                'health': enemy.health,
                'energy': enemy.energy
            }
            enemies_context.append(enemy_context)
    else:
        enemy_context = {
            'name': enemies.name,
            'health': enemies.health,
            'energy': enemies.energy
        }
        enemies_context.append(enemy_context)

    return enemies_context


def get_exp_for_kill(hero, enemy):
    base_exp = 100
    exp_modifier = 1
    level_bonus = 0

    level_difference = enemy.level - hero.level

    if level_difference > 0 and level_difference <= 3:
        exp_modifier = 1.3
        base_exp = 150
    elif level_difference > 3 and level_difference <= 5:
        exp_modifier = 1.7
        base_exp = 250
    elif level_difference > 5 and level_difference <= 10:
        exp_modifier = 2
        base_exp = 450

    if enemy.level >= 2 and enemy.level <= 3:
        level_bonus = 100
    elif enemy.level >= 4 and enemy.level <= 6:
        level_bonus = 200

    print()
    print('Lvl diff: {}'.format(level_difference))
    print('Base exp: {}'.format(base_exp))
    print('Exp mult: {}'.format(hero.exp_multiplier))
    print('Exp modifier: {}'.format(exp_modifier))
    print('Lvl bonus: {}'.format(level_bonus))

    print('Curr exp: {}'.format(hero.exp))

    print()

    exp = round(base_exp * hero.exp_multiplier * exp_modifier + level_bonus)
    print('You got {0} exp'.format(exp))
    hero.exp += exp

    print('After exp: {}'.format(hero.exp))



def hit_chance(attacking_character, defending_character):
    print('Attacking agility: {}'.format(attacking_character.agility))
    print('Defending agility: {}'.format(defending_character.agility))
    chance = round(((attacking_character.agility - defending_character.agility) / attacking_character.agility) * 100)

    if chance == 0:
        chance = randint(1, 50)
    elif chance < 0:
        chance = randint(1, 30)
    elif chance >= 100:
        chance = 80
    print('Hit chance: {0}'.format(chance))


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
    hit_chance(hero, enemy)
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


# TODO: change according on character sequence
def display_turn(turn, hero_name, enemy_name):
    if turn == 1:
        print('{0} begins'.format(hero_name))
    elif turn == 2:
        print('{0} begins'.format(enemy_name))


def display_enemy_choice(enemy_name, enemy_choice, damage):
    if isinstance(enemy_choice, str):
        print('{0} has hit you in {1}'.format(enemy_name, enemy_choice))
        print('You received {0} damage'.format(damage))


def display_characters_info(hero, enemy):
    print('{0}: {1} {4:>20}: {5}\n{2}: {3}\n'.format('Your health', hero.health, 'Your energy', hero.energy,
                                                     'Enemy health', enemy.health))


def choose_enemy(enemies: list):
    enemies = [character for character in enemies if not isinstance(character, Hero)]

    if len(enemies) == 1:
        return enemies[0]

    while True:
        for i, enemy in enumerate(enemies):
            print('{0}: {1} ({2}/{3})'.format(i + 1, enemy.name, enemy.health, enemy.max_health))

        cmd = get_cmd()

        try:
            cmd = int(cmd)

            if cmd > 0:
                return enemies[int(cmd) - 1]
        except ValueError:
            display_incorrect_command()
        except IndexError:
            display_incorrect_command()


def is_many_enemies(enemy):
    if isinstance(enemy, Enemy):
        return False
    elif isinstance(enemy, list):
        return True
    else:
        exit()


def is_enemy_dead(enemy):
    if enemy.health <= 0:
        return True
    else:
        return False


def is_hero_dead(hero):
    if hero.health <= 0:
        return True
    else:
        return False


def is_hero(character):
    if isinstance(character, Hero):
        return True
    elif isinstance(character, Enemy):
        return False
    else:
        # TODO: create class with exit codes using Enum module
        exit()


def count_enemies(queue: list):
    enemies_count = 0

    for character in queue:
        if isinstance(character, Enemy):
            enemies_count += 1

    return enemies_count


def make_queue(hero, enemies):
    characters = [hero]

    is_many = is_many_enemies(enemies)

    if is_many:
        characters += enemies[1:]
    elif not is_many:
        characters.append(enemies)

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


def display_versus(hero, enemies):
    is_many = is_many_enemies(enemies)

    if is_many:
        print('{0} VS {1}'.format(hero.name, enemies[0]))
    elif not is_many:
        print('{0} VS {1}'.format(hero.name, enemies.name))


def battle(hero, enemies):
    display_title('Battle')
    display_versus(hero=hero, enemies=enemies)

    queue = make_queue(hero=hero, enemies=enemies)

    enemies_count = count_enemies(queue)

    enemies_context = save_enemies_context(enemies[1:]) if isinstance(enemies, list) else save_enemies_context(enemies)

    while enemies_count != 0:
        for character in queue:
            if is_hero(character):
                enemy = choose_enemy(queue)
                display_characters_info(hero=hero, enemy=enemy)
                hero_action(hero=hero, enemy=enemy)

                if is_enemy_dead(enemy=enemy):
                    queue.remove(enemy)
                    enemies_count -= 1
                    get_exp_for_kill(hero=hero, enemy=enemy)
                    hero.gold += enemy.gold
            else:
                enemy_action(hero=hero, enemy=character)

                if is_hero_dead(hero):
                    return_enemies_context(enemies[1:], enemies_context) if isinstance(enemies, list) else \
                        return_enemies_context(enemies, enemies_context)
                    display_title("You lose!")
                    return False

    display_title("You're a winner!")
    return True
