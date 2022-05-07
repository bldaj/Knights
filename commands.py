import abc


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
