from commands.common import (
    BaseCommand,
)
from menus.main_menu import (
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
        self.main_menu = MainMenu()

    def start(self):
        """
        Starts main game loop
        """
        while True:
            self.main_menu.run()


if __name__ == '__main__':
    game = Game()
    game.start()
