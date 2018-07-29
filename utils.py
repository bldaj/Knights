def display_title(title):
    print('\n{0:^40}\n'.format(title))


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
