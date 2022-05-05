import abc


# Commands

class BaseCommand(abc.ABC):
    """
    """

    @abc.abstractmethod
    def execute(self):
        pass


class NewGameCommand(BaseCommand):
    """
    """

    def __init__(self):
        self.title = 'New game'

    def execute(self):
        print(f'{self.title} chosen')


class SaveGameCommand(BaseCommand):
    """
    """

    def __init__(self):
        self.title = 'Save game'

    def execute(self):
        print(f'{self.title} chosen')


class LoadGameCommand(BaseCommand):
    """
    """

    def __init__(self):
        self.title = 'Load game'

    def execute(self):
        print(f'{self.title} chosen')


class ExitGameCommand(BaseCommand):
    """
    """

    def __init__(self):
        self.title = 'Exit game'

    def execute(self):
        exit('Game exited')


# Menu

class BaseMenu(abc.ABC):
    """
    """

    @abc.abstractmethod
    def run(self) -> None:
        pass

    def print_commands(self) -> None:
        """
        Prints available commands (self._commands param)
        """
        for i, command in enumerate(self._commands, start=1):
            print(f'[{i}] {command.title}')

    def exec_command(self, user_cmd):
        try:
            self._commands[user_cmd].execute()

        # TODO: Specify list of exceptions
        except Exception:
            print('Incorrect command')

    def get_user_cmd(self):
        try:
            cmd = int(input('Enter your choice: '))
            cmd -= 1
        except ValueError:
            # TODO: Add common message
            print('Incorrect command')
        else:
            self.exec_command(cmd)


class MainMenu(BaseMenu):

    def __init__(self):
        self._commands = [
            NewGameCommand(),
            LoadGameCommand(),
            SaveGameCommand(),
            ExitGameCommand(),
        ]

    def run(self):
        while True:
            self.print_commands()
            self.get_user_cmd()


# Game

class CommandStack:
    """
    Stores history of executed command
    """

    def __init__(self):
        self._stack = []

    def add(self, command: BaseCommand):
        self._stack.append(command)

    def pop(self):
        return self._stack.pop()


class Game:
    """
    Main class to start game
    """

    def __init__(self):
        self._command_stack = CommandStack()
        self._main_menu = MainMenu()

    def on_start(self):
        self._main_menu.run()

    def on_exit(self):
        pass

    def start(self):
        """
        Starts main game loop
        """
        self.on_start()
        self.on_exit()


if __name__ == '__main__':
    game = Game()
    game.start()
