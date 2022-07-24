import abc


class BaseCharacter(abc.ABC):
    """
    """

    def __init__(
            self,
            name: str,
            level: int,
            exp: int,
            health: int,
            mental_health: int,
            energy: int,
            mana: int,
            strength: int,
            agility: int,
            intelligence: int,
            luck: int,
            physical_resistance: int,
            magic_resistance: int,
            poison_resistance: int,
            spirit_resistance: int,
            hostility: int,
    ):
        self.name = name
        self.level = level
        self.exp = exp

        self.health = health
        self.max_health = health

        self.mental_health = mental_health
        self.max_mental_health = mental_health

        self.energy = energy
        self.max_energy = energy

        self.mana = mana
        self.max_mana = mana

        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        self.luck = luck

        self.health_regen = None
        self.energy_regen = None
        self.mana_regen = None

        self.physical_resistance = physical_resistance
        self.magic_resistance = magic_resistance
        self.poison_resistance = poison_resistance
        self.spirit_resistance = spirit_resistance  # includes mind reading

        self.armor = None   # TBD: get from init or calculate?
        self.current_damage = None  # calculate it
        self.state = None   # like healthy, sick, wounded

        self.inventory = []

        self.hostility = hostility

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


class BaseHero(BaseCharacter, abc.ABC):
    """
    """


class BaseEnemy(BaseCharacter, abc.ABC):
    """
    """


class BaseNPC(BaseCharacter, abc.ABC):
    """
    """
