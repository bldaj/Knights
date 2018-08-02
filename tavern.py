from time import sleep
from random import randint

from utils import display_title, display_greeting, display_commands, get_cmd, display_incorrect_command
from constants import CHEAP_ROOM_LUCK_MODIFIER, WELL_MAINTAINED_ROOM_LUCK_MODIFIER, LUXURY_ROOM_LUCK_MODIFIER
from constants import CHEAP_ROOM_ROB_PERCENTAGE, WELL_MAINTAINED_ROOM_ROB_PERCENTAGE, LUXURY_ROOM_ROB_PERCENTAGE


def _be_robbed(hero, rob_percentage):
    stolen_gold = (hero.gold * rob_percentage) / 100

    hero.gold - stolen_gold
    print('You were robbed while you slept.\nYou lost {0} gold'.format(stolen_gold))


def _limit_health_and_energy(hero):
    if hero.health > hero.max_health:
        hero.health = hero.max_health

    if hero.energy > hero.max_energy:
        hero.energy = hero.max_energy


def _sleep(hero, room_level):
    print('You fell asleep right in the equipment')

    count = 0
    modifier = 1

    if room_level == 'low':
        modifier = 3
    elif room_level == 'middle':
        modifier = 5
    elif modifier == 'high':
        modifier = 10

    while count <= 5:
        hero.health += hero.hp_regen * modifier
        hero.energy += hero.energy_regen * modifier
        count += 1
        sleep(1)

    _limit_health_and_energy(hero)


def _event(hero, luck_modifier, rob_percentage):
    chance = hero.luck * luck_modifier

    print('Chance be robbed: {0}'.format(chance))

    if chance < randint(1, 100):
        _be_robbed(hero=hero, rob_percentage=rob_percentage)
        return True
    else:
        return False


def _luxury_room(hero):
    _sleep(hero=hero, room_level='high')
    if _event(hero=hero, luck_modifier=LUXURY_ROOM_LUCK_MODIFIER,
              rob_percentage=LUXURY_ROOM_ROB_PERCENTAGE):
        print("You slept well, but after the discovery of the loss you're sad")
    else:
        print("You feel well-rested yourself")


def _well_maintained_room(hero):
    _sleep(hero=hero, room_level='middle')
    if _event(hero=hero, luck_modifier=WELL_MAINTAINED_ROOM_LUCK_MODIFIER,
              rob_percentage=WELL_MAINTAINED_ROOM_ROB_PERCENTAGE):
        print('You slept almost well, but loss money makes you angry')
    else:
        print("You're rested quite good")


def _cheap_room(hero):
    _sleep(hero=hero, room_level='low')
    if _event(hero=hero, luck_modifier=CHEAP_ROOM_LUCK_MODIFIER,
              rob_percentage=CHEAP_ROOM_ROB_PERCENTAGE):
        print("Heck! I not only did sleep on a hard bed, but also I'm robbed")
    else:
        print('I need fight hard to not return back here again...')


def _have_a_drink(hero):
    pass


def _rent_room(hero):
    cheap_room_cost = 5
    well_maintained_room_cost = 12
    luxury_room_cost = 30

    while True:
        print('\nYour health: {0}/{1}\nYour energy: {2}/{3}\nYou have {4} gold\n'.format(
            hero.health, hero.max_health,
            hero.energy, hero.max_energy,
            hero.gold
        ))

        display_commands(commands=[
            'Rent cheap room {0} gold'.format(cheap_room_cost),
            'Rent well-maintained room {0} gold'.format(well_maintained_room_cost),
            'Rent luxury room {0} gold'.format(luxury_room_cost),
            'Back to the previous menu'
        ])

        cmd = get_cmd(message='What room would you rent?')

        if cmd == '1':
            _cheap_room(hero)
        elif cmd == '2':
            _well_maintained_room(hero)
        elif cmd == '3':
            _luxury_room(hero)
        elif cmd == '4':
            return
        else:
            display_incorrect_command()


def tavern(hero):
    display_title('Tavern')
    display_greeting()

    while True:
        display_commands(commands=[
            'Rent the room',
            "Wet one's whistle",
            'Back to the previous menu'
        ])

        cmd = get_cmd(message='What do you want?')

        if cmd == '1':
            _rent_room(hero)
        elif cmd == '2':
            print("Are you kidding me? I wanna sleep! Let's rent a room...")
        elif cmd == '3':
            return
        else:
            display_incorrect_command()
