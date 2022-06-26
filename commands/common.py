import abc


class BaseCommand(abc.ABC):
    """
    """

    title: str = ''

    @abc.abstractmethod
    def execute(self):
        pass
