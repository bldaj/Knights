import abc

from commands import (
    NewGameCommand,
    LoadGameCommand,
    SaveGameCommand,
    ExitGameCommand,
)


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
