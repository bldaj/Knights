from utils import display_title, display_greeting, display_commands, get_cmd, display_incorrect_command


def _rent_room(hero):
    cheap_room_cost = 5
    well_groomed_room_cost = 12
    luxury_room_cost = 30

    while True:
        print('\nYour health: {0}/{1}\nYour energy: {2}/{3}\nYou have {4} gold\n'.format(
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
    display_title('Tavern')
    display_greeting()

    while True:
        display_commands(commands=[
            'Rent the room',
            'Have a drink',
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
