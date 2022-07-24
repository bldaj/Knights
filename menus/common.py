import abc

from commands.common import (
    BaseCommand,
)
from strings import (
    errors,
)


class BaseMenu(abc.ABC):
    """
    """

    commands: list[BaseCommand] | tuple[BaseCommand] = ()

    def _validate_commands(self):
        for command in self.commands:
            if not isinstance(command, BaseCommand):
                print(errors.INCORRECT_COMMAND_INITIALIZATION.format(command=command))

    def print_commands(self) -> None:
        """
        Prints available commands (BaseMenu.commands attribute)

        Example:
            [1]: Sleep
            [2]: Sleep
            [3]: More sleep
        """
        for i, command in enumerate(self.commands, start=1):
            print(f'[{i}]: {command.title}')

    def get_user_command(self):
        try:
            user_cmd = int(input('Enter your choice: '))
            user_cmd -= 1
        except ValueError:
            print(errors.INCORRECT_COMMAND)
        else:
            return user_cmd

    def exec_command(self):
        """
        """
        user_cmd = self.get_user_command()

        try:
            command = self.commands[user_cmd]()
            command.execute()

        # TODO: Specify list of exceptions
        except Exception as e:
            print(e)
            print(errors.INCORRECT_COMMAND)

    def run(self) -> None:
        """
        Main entry point
        """
        while True:
            self.print_commands()
            self.exec_command()
