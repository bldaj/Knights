import abc


class BaseCommand(abc.ABC):
    """
    """

    title: str = ''

    @abc.abstractmethod
    def execute(self):
        pass


class NewGameCommand(BaseCommand):
    """
    """

    title = 'New game'

    def execute(self):
        print(f'{self.title} chosen')


class SaveGameCommand(BaseCommand):
    """
    """

    title = 'Save game'

    def execute(self):
        print(f'{self.title} chosen')


class LoadGameCommand(BaseCommand):
    """
    """

    title = 'Load game'

    def execute(self):
        print(f'{self.title} chosen')


class ExitGameCommand(BaseCommand):
    """
    """

    title = 'Exit game'

    def execute(self):
        exit('Game exited')
