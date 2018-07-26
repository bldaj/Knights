class Armor:
    def __init__(self, type, name, protection_value, armor_level, rarity, durability):
        self.type = type
        self.name = name
        self.protection = protection_value
        self.armor_level = armor_level
        self.rarity =rarity
        self.durability = durability
        self.additional_effects = {}
