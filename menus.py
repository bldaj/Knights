import abc

from commands import (
    NewGameCommand,
    LoadGameCommand,
    SaveGameCommand,
    ExitGameCommand,
)
from strings import errors


class BaseMenu(abc.ABC):
    """
    """

    commands: list | tuple = ()

    @abc.abstractmethod
    def run(self) -> None:
        pass

    def print_commands(self) -> None:
        """
        Prints available commands (self._commands param)
        """
        for i, command in enumerate(self.commands, start=1):
            print(f'[{i}] {command.title}')

    def exec_command(self, user_cmd: int):
        try:
            command = self.commands[user_cmd]()
            command.execute()

        # TODO: Specify list of exceptions
        except Exception as e:
            print(e)
            print(errors.INCORRECT_COMMAND)

    def get_user_cmd(self):
        try:
            cmd = int(input('Enter your choice: '))
            cmd -= 1
        except ValueError:
            # TODO: Add common message
            print(errors.INCORRECT_COMMAND)
        else:
            self.exec_command(cmd)


class MainMenu(BaseMenu):
    """
    """

    commands = [
        NewGameCommand,
        LoadGameCommand,
        SaveGameCommand,
        ExitGameCommand,
    ]

    def run(self):
        while True:
            self.print_commands()
            self.get_user_cmd()
