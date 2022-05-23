import abc


class BaseCharacter(abc.ABC):
    """
    """

    def __init__(
            self,
            name: str,
            health: int,
            energy: int,
    ):
        self.name = name
        self.health = health
        self.energy = energy

    def _move_left(self):
        pass

    def _move_right(self):
        pass

    def _move_up(self):
        pass

    def _move_down(self):
        pass

    @abc.abstractmethod
    def move(self):
        """
        """
        pass

    @abc.abstractmethod
    def attack(self):
        pass
