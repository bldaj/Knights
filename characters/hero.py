import abc

from characters.base import (
    BaseCharacter,
)


class BaseHero(BaseCharacter, abc.ABC):
    """
    """

    def __init__(
            self,
            name: str,
            level: int = 1,
            health: int = 100,
            mental_health: int = 100,
            energy: int = 100,
            mana: int = 100,
            strength: int = 10,
            agility: int = 10,
            intelligence: int = 10,
            luck: int = 10,
            hostility: int = 0,
    ):
        super(BaseHero, self).__init__(
            name=name,
            level=level,
            health=health,
            mental_health=mental_health,
            energy=energy,
            mana=mana,
            strength=strength,
            agility=agility,
            intelligence=intelligence,
            luck=luck,
            hostility=hostility,
        )


class Hero(BaseHero):
    """
    """

    def move(self):
        """
        """
        pass

    def attack(self):
        """
        """
        pass
