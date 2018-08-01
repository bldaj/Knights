from utils import display_commands, get_cmd, display_incorrect_command


def _rent_room(hero):
    cheap_room_cost = 5
    well_groomed_room_cost = 12
    luxury_room_cost = 30

    while True:
        print('Your health: {0}/{1}\nYour energy: {2}/{3}\nYou have {4} gold'.format(
            hero.health, hero.max_health,
            hero.energy, hero.max_energy,
            hero.gold
        ))

        display_commands(commands=[
            'Rent cheap room {0} gold'.format(cheap_room_cost),
            'Rent well-groomed room room {0} gold'.format(well_groomed_room_cost),
            'Rent luxury room room {0} gold'.format(luxury_room_cost),
            'Back to the previous menu'
        ])

        cmd = get_cmd(message='What room would you rent?')

        if cmd == '1':
            pass
        elif cmd == '2':
            pass
        elif cmd == '3':
            pass
        elif cmd == '4':
            return
        else:
            display_incorrect_command()


def tavern(hero):
    while True:
        display_commands(commands=[
            'Rent the room'
        ])

        cmd = get_cmd(message='Hello, traveler!\nWhat do you want?')

        if cmd == '1':
            _rent_room(hero)
        else:
            display_incorrect_command()
