from utils import display_commands, get_cmd, display_incorrect_command


def _limit_energy_value(hero):
    if hero.energy > hero.max_energy:
        hero.energy = hero.max_energy


def _rest(hero, rest_value, cost):
    if hero.energy != hero.max_energy:
        if hero.energy < 0:
            hero.energy = 0

        hero.energy += rest_value
        _limit_energy_value(hero)
        hero.gold -= cost
    else:
        print("You're full rested, get out here!")


# TODO: move it to utils module
def _check_hero_gold(hero_gold, cost):
    if hero_gold >= cost:
        return True
    else:
        return False


def take_a_rest(hero):
    low_level_hotel_rest_value = 15
    middle_level_hotel_rest_value = 40
    high_level_hotel_rest_value = 150

    low_level_hotel_cost = 5
    middle_level_hotel_cost = 10
    high_level_hotel_cost = 30

    while True:
        print('Your energy: {0}/{1}\nYou have {2} gold'.format(hero.energy, hero.max_energy, hero.gold))

        display_commands(commands=[
            'Stay at low level hotel ({0} energy/{1} gold/{2}% chance to be robbed)'.format(
                low_level_hotel_rest_value,
                low_level_hotel_cost,
                0
            ),
            'Stay at middle level hotel ({0} energy/{1} gold/{2}% chance to be robbed)'.format(
                middle_level_hotel_rest_value,
                middle_level_hotel_cost,
                0
            ),
            'Stay at high level hotel ({0} energy/{1} gold/{2}% chance to be robbed)'.format(
                high_level_hotel_rest_value,
                high_level_hotel_cost,
                0
            ),
            'Back to the previous menu'
        ])

        cmd = get_cmd()

        if cmd == '1':
            if _check_hero_gold(hero_gold=hero.gold, cost=low_level_hotel_cost):
                _rest(hero=hero, rest_value=low_level_hotel_rest_value, cost=low_level_hotel_cost)
            else:
                # TODO: move it to utils module in own function
                print("You don't have enough money")
        elif cmd == '2':
            if _check_hero_gold(hero_gold=hero.gold, cost=middle_level_hotel_cost):
                _rest(hero=hero, rest_value=middle_level_hotel_rest_value, cost=middle_level_hotel_cost)
            else:
                print("You don't have enough money")
        elif cmd == '3':
            if _check_hero_gold(hero_gold=hero.gold, cost=high_level_hotel_cost):
                _rest(hero=hero, rest_value=high_level_hotel_rest_value, cost=high_level_hotel_cost)
            else:
                print("You don't have enough money")
        elif cmd == '4':
            return
        else:
            display_incorrect_command()
