from utils import *


def town_menu(hero, enemies: list):
    display_title('Town')

    print(hero.name, hero.health)

    for e in enemies:
        print(e.name, e.health)

    commands = ['Main menu']

    display_commands(commands)

    cmd = get_cmd()

    if cmd == '1':
        from main import main_menu

        main_menu()
