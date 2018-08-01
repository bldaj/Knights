from utils import display_commands, get_cmd, display_incorrect_command


def take_a_rest(hero):
    while True:
        display_commands(commands=['Stay at low level hotel', 'Stay at middle level hotel', 'Stay at high level hotel',
                                   'Back to the previous menu'])

        cmd = get_cmd()

        if cmd == '1':
            pass
        elif cmd == '2':
            pass
        elif cmd == '3':
            pass
        elif cmd == '4':
            return
