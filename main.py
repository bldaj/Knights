import abc


# Commands

class BaseCommand(abc.ABC):
    """
    """

    @abc.abstractmethod
    def execute(self):
        pass

    @property
    def title(self):
        return self.__class__.__name__


class NewGameCommand(BaseCommand):
    """
    """

    def execute(self):
        pass


class SaveGameCommand(BaseCommand):
    """
    """

    def execute(self):
        pass


class LoadGameCommand(BaseCommand):
    """
    """

    def execute(self):
        pass


class ExitGameCommand(BaseCommand):
    """
    """

    def execute(self):
        exit('Game exited')


# Menu


class BaseMenu(abc.ABC):

    def __int__(self):
        self._commands: list[BaseCommand] = []

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
        except ValueError:
            # TODO: Add common message
            print('Incorrect command')

            # Завершить вызов команд и обработку исключений


class MainMenu(BaseMenu):

    def __init__(self):
        self._commands = [
            NewGameCommand,
            LoadGameCommand,
            SaveGameCommand,
            ExitGameCommand,
        ]

    def run(self):
        self.print_commands()

    def print_commands(self):
        for i, command in enumerate(self._commands, start=1):
            print(f'[{i}] {command.title}')


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
