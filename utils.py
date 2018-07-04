def display_title(title):
    print('{0:^20}\n'.format(title))


def display_incorrect_command():
    print('Incorrect command')


def display_commands(commands):
    for i, command in enumerate(commands):
        print('[%d]: %s' % (i+1, command))


def get_cmd():
    return input('Make your choice: ')
