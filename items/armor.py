class Armor:
    def __init__(self, type, name, description, protection_value, armor_level=1, rarity=1, durability=100):
        self.type = type
        self.name = name
        self.description = description
        self.protection = protection_value
        self.armor_level = armor_level
        self.rarity = rarity
        self.durability = durability
        self.additional_effects = {}


tunic = Armor(type='breastplate', name='Tunic', description='Light tunic', protection_value=1)
light_boots = Armor(type='boots', name='Light boots', description='Light boots', protection_value=1)
