def print_title(title):
    print('{:^20}'.format(title))


def show_commands(commands):
    for i, command in enumerate(commands):
        print('[%d]: %s' % (i+1, command))
