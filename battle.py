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

    exp = round(base_exp * hero.exp_multiplier * exp_modifier + level_bonus)
    hero.exp += exp

    print('You got {0} exp'.format(exp))


def calculate_hit_chance(attacking_character, defending_character, place_to_attack: str):
    agility_difference = attacking_character.agility - defending_character.agility

    if agility_difference > 0:
        chance = round((agility_difference / attacking_character.agility) * 100)

        if place_to_attack == 'head':
            chance = round(chance * HEAD_HIT_MODIFIER)
        elif place_to_attack == 'body':
            chance = round(chance * BODY_HIT_MODIFIER)
        elif place_to_attack == 'arms':
            chance = round(chance * ARMS_HIT_MODIFIER)
        elif place_to_attack == 'legs':
            chance = round(chance * LEGS_HIT_MODIFIER)

        return chance
    else:
        return randint(1, 40)


def analyze_hit_chance(chance, place_to_attack: str):
    if chance > 100:
        chance = 99

    if place_to_attack == 'head' and chance < HEAD_HIT_CHANCE:
        chance = HEAD_HIT_CHANCE
    elif place_to_attack == 'body' and chance < BODY_HIT_CHANCE:
        chance = BODY_HIT_CHANCE
    elif place_to_attack == 'arms' and chance < ARMS_HIT_CHANCE:
        chance = ARMS_HIT_CHANCE
    elif place_to_attack == 'legs' and chance < LEGS_HIT_CHANCE:
        chance = LEGS_HIT_CHANCE

    return chance


def enemy_action_logic(chances: dict, damages: dict) -> str:
    sorted_chances = sorted((v, k) for (k, v) in chances.items())

    max_damage = 0
    max_chance = 0
    enemy_choice = None

    for chance in sorted_chances:
        if chance[0] > max_chance:
            max_chance = chance[0]
            enemy_choice = chance[1]
        elif chance[0] == max_chance:
            # TODO: add analyze enemy damage and energy and hero health and armor for equal hit chances
            pass

    return enemy_choice


def enemy_action(hero, enemy):
    head_hit_chance = calculate_hit_chance(attacking_character=enemy, defending_character=hero, place_to_attack='head')
    body_hit_chance = calculate_hit_chance(attacking_character=enemy, defending_character=hero, place_to_attack='body')
    arms_hit_chance = calculate_hit_chance(attacking_character=enemy, defending_character=hero, place_to_attack='arms')
    legs_hit_chance = calculate_hit_chance(attacking_character=enemy, defending_character=hero, place_to_attack='legs')

    head_armor = 0
    if hero.helmet is not None:
        head_armor = hero.helmet.protection

    body_armor = 0
    if hero.breastplate is not None:
        body_armor = hero.breastplate.protection

    arms_armor = 0
    if hero.bracers is not None:
        arms_armor = hero.bracers.protection

    legs_armor = 0
    if hero.boots is not None:
        legs_armor = hero.boots.protection

    head_damage = int((40 + enemy.strength * HEAD_DAMAGE_MODIFIER) - hero.physical_resistance - head_armor)
    body_damage = int((30 + enemy.strength * BODY_DAMAGE_MODIFIER) - hero.physical_resistance - body_armor)
    arms_damage = int((20 + enemy.strength * ARMS_DAMAGE_MODIFIER) - hero.physical_resistance - arms_armor)
    legs_damage = int((20 + enemy.strength * LEGS_DAMAGE_MODIFIER) - hero.physical_resistance - legs_armor)

    if head_damage < 0:
        head_damage = 0

    if body_damage < 0:
        body_damage = 0

    if arms_damage < 0:
        arms_damage = 0

    if legs_damage < 0:
        legs_damage = 0

    cmd = enemy_action_logic(chances={'head': head_hit_chance,
                                      'body': body_hit_chance,
                                      'arms': arms_hit_chance,
                                      'legs': legs_hit_chance},
                             damages={'head': head_damage,
                                      'body': body_damage,
                                      'arms': arms_damage,
                                      'legs': legs_damage}
                             )

    if cmd == 'head':
        if head_hit_chance >= randint(1, 100):
            enemy.energy -= 15

            if hero.helmet is not None:
                hero.helmet.durability -= 0

            hero.health -= head_damage

            display_enemy_choice(enemy.name, 'head', head_damage)
        else:
            display_enemy_miss(enemy.name)

    elif cmd == 'body':
        if body_hit_chance >= randint(1, 100):
            enemy.energy -= 10

            if hero.breastplate is not None:
                hero.breastplate.durability -= 0

            hero.health -= body_damage

            display_enemy_choice(enemy.name, 'body', body_damage)
        else:
            display_enemy_miss(enemy.name)

    elif cmd == 'arms':
        if arms_hit_chance >= randint(1, 100):
            enemy.energy -= 7

            if hero.bracers is not None:
                hero.bracers.durability -= 0

            hero.health -= arms_damage

            display_enemy_choice(enemy.name, 'arms', arms_damage)
        else:
            display_enemy_miss(enemy.name)

    elif cmd == 'legs':
        if legs_hit_chance >= randint(1, 100):
            enemy.energy -= 7

            if hero.boots is not None:
                hero.boots.durability -= 0

            hero.health -= legs_damage

            display_enemy_choice(enemy.name, 'legs', legs_damage)
        else:
            display_enemy_miss(enemy.name)


def hero_action(hero, enemy):
    head_hit_chance = calculate_hit_chance(attacking_character=hero, defending_character=enemy, place_to_attack='head')
    body_hit_chance = calculate_hit_chance(attacking_character=hero, defending_character=enemy, place_to_attack='body')
    arms_hit_chance = calculate_hit_chance(attacking_character=hero, defending_character=enemy, place_to_attack='arms')
    legs_hit_chance = calculate_hit_chance(attacking_character=hero, defending_character=enemy, place_to_attack='legs')

    head_hit_chance = analyze_hit_chance(chance=head_hit_chance, place_to_attack='head')
    body_hit_chance = analyze_hit_chance(chance=body_hit_chance, place_to_attack='body')
    arms_hit_chance = analyze_hit_chance(chance=arms_hit_chance, place_to_attack='arms')
    legs_hit_chance = analyze_hit_chance(chance=legs_hit_chance, place_to_attack='legs')

    enemy_head_armor = 0
    enemy_body_armor = 0
    enemy_arms_armor = 0
    enemy_legs_armor = 0

    if enemy.helmet is not None:
        enemy_head_armor = enemy.helmet.protection

    if enemy.breastplate is not None:
        enemy_body_armor = enemy.breastplate.protection

    if enemy.bracers is not None:
        enemy_arms_armor = enemy.bracers.protection

    if enemy.boots is not None:
        enemy_legs_armor = enemy.boots.protection

    head_damage = int((40 + hero.strength * HEAD_DAMAGE_MODIFIER) - enemy.physical_resistance - enemy_head_armor)
    body_damage = int((30 + hero.strength * BODY_DAMAGE_MODIFIER) - enemy.physical_resistance - enemy_body_armor)
    arms_damage = int((20 + hero.strength * ARMS_DAMAGE_MODIFIER) - enemy.physical_resistance - enemy_arms_armor)
    legs_damage = int((20 + hero.strength * LEGS_DAMAGE_MODIFIER) - enemy.physical_resistance - enemy_legs_armor)

    display_commands(['Hit in head ({0} dmg/{1} energy) ({2}% chance)'.format(head_damage, 15, head_hit_chance),
                      'Hit in body ({0} dmg/{1} energy) ({2}% chance)'.format(body_damage, 10, body_hit_chance),
                      'Hit in arms ({0} dmg/{1} energy) ({2}% chance)'.format(arms_damage, 7, arms_hit_chance),
                      'Hit in legs ({0} dmg/{1} energy) ({2}% chance)'.format(legs_damage, 7, legs_hit_chance),
                      'Block'])

    cmd = get_cmd()

    if cmd == '1':
        if head_hit_chance >= randint(1, 100):
            enemy.health -= head_damage
            display_delivered_damage(head_damage)

            if enemy.helmet is not None:
                enemy.helmet.durability -= 0
        else:
            print('\nMiss')
        hero.energy -= 15

    elif cmd == '2':
        if body_hit_chance >= randint(1, 100):
            enemy.health -= body_damage
            display_delivered_damage(body_damage)

            if enemy.breastplate is not None:
                enemy.breastplate.durability -= 0
        else:
            print('\nMiss')
        hero.energy -= 10

    elif cmd == '3':
        if arms_hit_chance >= randint(1, 100):
            enemy.health -= arms_damage
            display_delivered_damage(arms_damage)

            if enemy.bracers is not None:
                enemy.bracers.durability -= 0
        else:
            print('\nMiss')
        hero.energy -= 7

    elif cmd == '4':
        if legs_hit_chance >= randint(1, 100):
            enemy.health -= legs_damage
            display_delivered_damage(legs_damage)

            if enemy.boots is not None:
                enemy.boots.durability -= 0
        else:
            print('\nMiss')
        hero.energy -= 7

    elif cmd == '5':
        print('\nOh, man, it seems that I have nothing to block...')
        hero_action(hero=hero, enemy=enemy)

    else:
        display_incorrect_command()
        hero_action(hero=hero, enemy=enemy)


def display_delivered_damage(damage_value):
    print("\nYou've delivered {0} damage".format(damage_value))


# TODO: change according on character sequence
def display_turn(turn, hero_name, enemy_name):
    if turn == 1:
        print('{0} begins'.format(hero_name))
    elif turn == 2:
        print('{0} begins'.format(enemy_name))


def display_enemy_miss(enemy_name: str):
    print('\n{0} has missed'.format(enemy_name))


def display_enemy_choice(enemy_name, enemy_choice, damage):
    if isinstance(enemy_choice, str):
        print('\n{0} has hit you in {1}'.format(enemy_name, enemy_choice))
        print('You received {0} damage'.format(damage))


def display_characters_info(hero, enemy):
    print('\n{0}: {1} {4:>20}: {5}\n{2}: {3}\n'.format('Your health', hero.health, 'Your energy', hero.energy,
                                                       'Enemy health', enemy.health))


def choose_enemy(enemies: list):
    enemies = [character for character in enemies if not isinstance(character, Hero)]

    if len(enemies) == 1:
        return enemies[0]

    while True:
        print()
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
        text = '{0} VS {1}'.format(hero.name, enemies[0])
        print('{0:^40}'.format(text))
    elif not is_many:
        text = '{0} VS {1}'.format(hero.name, enemies)
        print('{0:^40}'.format(text))


def battle(hero, enemies):
    display_title('Battle')
    display_versus(hero=hero, enemies=enemies)

    queue = make_queue(hero=hero, enemies=enemies)

    enemies_count = count_enemies(queue)

    enemies_context = save_enemies_context(enemies[1:]) if isinstance(enemies, list) else save_enemies_context(enemies)

    while enemies_count != 0:
        for character in queue:
            if is_hero(character):
                hero.health_regeneration()
                hero.energy_regeneration()

                enemy = choose_enemy(queue)
                display_characters_info(hero=hero, enemy=enemy)
                hero_action(hero=hero, enemy=enemy)

                if is_enemy_dead(enemy=enemy):
                    queue.remove(enemy)
                    enemies_count -= 1
                    get_exp_for_kill(hero=hero, enemy=enemy)
                    hero.gold += enemy.gold
            else:
                character.health_regeneration()
                character.energy_regeneration()

                enemy_action(hero=hero, enemy=character)

                if is_hero_dead(hero):
                    return_enemies_context(enemies[1:], enemies_context) if isinstance(enemies, list) else \
                        return_enemies_context(enemies, enemies_context)
                    display_battle_result("You lose!")
                    return False

    display_battle_result("You're the winner!")
    return True
