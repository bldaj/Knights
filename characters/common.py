import abc


class BaseCharacter(abc.ABC):
    """
    """

    def __init__(
            self,
            name: str,
            description: str,
            level: int,
            health: int,
            mental_health: int,
            energy: int,
            mana: int,
            strength: int,
            agility: int,
            intelligence: int,
            luck: int,
            hostility: int,
    ):
        self.name = name
        self.description = description

        self.level = level
        self.exp = self.calculate_exp_by_level()

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

        self.physical_resistance = self.calculate_physical_resistance()
        self.magic_resistance = self.calculate_magic_resistance()
        self.poison_resistance = self.calculate_poison_resistance()
        self.spirit_resistance = self.calculate_spirit_resistance()  # includes mind reading

        self.armor = None   # TBD: get from init or calculate?
        self.current_damage = None  # calculate it
        self.state = None   # like: healthy, sick, wounded

        self.inventory = []

        self.hostility = hostility

    def calculate_exp_by_level(self):
        pass

    def calculate_physical_resistance(self):
        pass

    def calculate_magic_resistance(self):
        pass

    def calculate_poison_resistance(self):
        pass

    def calculate_spirit_resistance(self):
        pass

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
