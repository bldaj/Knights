from random import randint


def display_title(title):
    print('\n{0:^40}\n'.format(title))


def display_greeting():
    greetings = [
        'Hello, traveler!',
        'Hello, stranger',
        "Ah, it's you again"
    ]

    greeting = greetings[randint(0, len(greetings) - 1)]
    print(greeting + '\n')


def display_incorrect_command():
    print('Incorrect command')


def display_battle_result(message_result: str):
    print('\n{0:^40}'.format(message_result))


def display_commands(commands: list):
    for i, command in enumerate(commands):
        print('[%d]: %s' % (i+1, command))


def display_load_successful():
    print('\nLoaded successfully')


def display_save_successful():
    print('\nSaved successfully')


def get_cmd(message='Make your choice: '):
    return input(message)


def check_money(hero_money, cost):
    if hero_money >= cost:
        return True
    else:
        return False
