def display_title(title):
    print('{0:^20}\n'.format(title))


def display_incorrect_command():
    print('Incorrect command')


def display_commands(commands: list):
    if isinstance(commands, list):
        for i, command in enumerate(commands):
            print('[%d]: %s' % (i+1, command))
    else:
        print('Commands are not list type')


def display_load_successful():
    print('Loaded successfully')


def display_save_successful():
    print('Saved successfully')


def get_cmd(message='Make your choice: '):
    return input(message)
