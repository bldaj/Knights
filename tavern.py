from time import sleep
from random import randint

from utils import display_title, display_greeting, display_commands, get_cmd, display_incorrect_command, check_money
from constants import CHEAP_ROOM_LUCK_MODIFIER, WELL_MAINTAINED_ROOM_LUCK_MODIFIER, LUXURY_ROOM_LUCK_MODIFIER
from constants import CHEAP_ROOM_ROB_PERCENTAGE, WELL_MAINTAINED_ROOM_ROB_PERCENTAGE, LUXURY_ROOM_ROB_PERCENTAGE


def pay_for_service(hero, cost):
    hero.gold = round(hero.gold - cost, 3)


def _be_robbed(hero, rob_percentage):
    stolen_gold = (hero.gold * rob_percentage) / 100

    hero.gold = round(hero.gold - stolen_gold, 3)
    print('\nYou were robbed while you slept.\nYou lost {0} gold'.format(stolen_gold))


def _limit_health_and_energy(hero):
    if hero.health > hero.max_health:
        hero.health = hero.max_health

    if hero.energy > hero.max_energy:
        hero.energy = hero.max_energy


def _sleep(hero, room_level):
    print('\nYou fell asleep right in the equipment.\nSleeping...')

    count = 0
    modifier = 1

    if room_level == 'low':
        modifier = 5

        hero.health += 10
        hero.energy += 10
    elif room_level == 'middle':
        modifier = 7

        hero.health += 20
        hero.energy += 20
    elif modifier == 'high':
        modifier = 10

        hero.health += 30
        hero.energy += 30
    while count <= 5:
        hero.health += hero.hp_regen * modifier
        hero.energy += hero.energy_regen * modifier
        count += 1
        sleep(1)

    hero.health = round(hero.health, 3)
    hero.energy = round(hero.energy, 3)

    _limit_health_and_energy(hero)


def _event(hero, luck_modifier, rob_percentage):
    chance = hero.luck * luck_modifier

    if chance < randint(1, 100):
        _be_robbed(hero=hero, rob_percentage=rob_percentage)
        return True
    else:
        return False


def _luxury_room(hero):
    _sleep(hero=hero, room_level='high')
    if _event(hero=hero, luck_modifier=LUXURY_ROOM_LUCK_MODIFIER,
              rob_percentage=LUXURY_ROOM_ROB_PERCENTAGE):
        print("\nYou slept well, but after the discovery of the loss you're sad")
    else:
        print("\nYou feel well-rested yourself")


def _well_maintained_room(hero):
    _sleep(hero=hero, room_level='middle')
    if _event(hero=hero, luck_modifier=WELL_MAINTAINED_ROOM_LUCK_MODIFIER,
              rob_percentage=WELL_MAINTAINED_ROOM_ROB_PERCENTAGE):
        print('\nYou slept almost well, but loss money makes you angry')
    else:
        print("\nYou're rested quite good")


def _cheap_room(hero):
    _sleep(hero=hero, room_level='low')
    if _event(hero=hero, luck_modifier=CHEAP_ROOM_LUCK_MODIFIER,
              rob_percentage=CHEAP_ROOM_ROB_PERCENTAGE):
        print("\nHeck! I not only did sleep on a hard bed, but also I'm robbed")
    else:
        print('\nI need fight hard to not return back here again...')


def _have_a_drink(hero):
    pass


def _rent_room(hero):
    cheap_room_cost = 5
    well_maintained_room_cost = 12
    luxury_room_cost = 30

    if hero.gold > 0:
        while True:
            print('\nYour health: {0}/{1}\nYour energy: {2}/{3}\nYou have {4} gold\n'.format(
                hero.health, hero.max_health,
                hero.energy, hero.max_energy,
                hero.gold
            ))

            display_commands(commands=[
                'Rent cheap room ({0} gold)'.format(cheap_room_cost),
                'Rent well-maintained room ({0} gold)'.format(well_maintained_room_cost),
                'Rent luxury room ({0} gold)'.format(luxury_room_cost),
                'Back to the previous menu'
            ])

            cmd = get_cmd(message='What room would you rent?\n')

            if cmd == '1':
                if check_money(hero_money=hero.gold, cost=cheap_room_cost):
                    pay_for_service(hero=hero, cost=cheap_room_cost)
                    _cheap_room(hero)
                else:
                    print('It seems like you have no enough gold')
            elif cmd == '2':
                if check_money(hero_money=hero.gold, cost=well_maintained_room_cost):
                    pay_for_service(hero=hero, cost=well_maintained_room_cost)
                    _well_maintained_room(hero)
                else:
                    print("Take a look at more cheap room, because you don't have enough gold")
            elif cmd == '3':
                if check_money(hero_money=hero.gold, cost=luxury_room_cost):
                    pay_for_service(hero=hero, cost=luxury_room_cost)
                    _luxury_room(hero)
                else:
                    print("Hahaha, son, are you kidding me? Thou don't have enough any gold!")
            elif cmd == '4':
                return
            else:
                display_incorrect_command()
    else:
        print('\nWhat did you forget here without money?! Get out!')


def tavern(hero):
    display_title('Tavern')
    display_greeting()

    while True:
        display_commands(commands=[
            'Rent the room',
            "Wet one's whistle",
            'Back to the previous menu'
        ])

        cmd = get_cmd(message='What do you want?\n')

        if cmd == '1':
            _rent_room(hero)
        elif cmd == '2':
            print("\nAre you kidding me? I wanna sleep! Let's rent a room...")
        elif cmd == '3':
            return
        else:
            display_incorrect_command()
