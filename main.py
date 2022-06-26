from commands.common import (
    BaseCommand,
)
from menus import (
    MainMenu,
)


class CommandStack:
    """
    Stores history of executed command
    """

    def __init__(self, limit=5):
        self._stack = []
        self.limit = limit

    def add(self, command: BaseCommand):
        self._stack.append(command)

        if len(self._stack) > self.limit:
            self._stack.remove(self._stack[0])

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
