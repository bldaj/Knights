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

    @abc.abstractmethod
    def attack(self):
        pass
