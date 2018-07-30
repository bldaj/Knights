class Armor:
    def __init__(self, type_, name, description, protection_value, armor_level=1, rarity=1, durability=100,
                 additional_effects=()):
        self.type = type_
        self.name = name
        self.description = description
        self.protection = protection_value
        self.armor_level = armor_level
        self.rarity = rarity
        self.durability = durability
        self.additional_effects = additional_effects


# Head armor
leather_helmet = Armor(type_='helmet', name='Leather helmet', description='Leather helmet', protection_value=2,
                       additional_effects=(
                           {'agility': 1}
                       ))


# Body armor
tunic = Armor(type_='breastplate', name='Tunic', description='Tunic', protection_value=1)
gambeson = Armor(type_='breastplate', name='Gambeson', description='Gambeson', protection_value=5)

# Arms armor
leather_bracers = Armor(type_='bracers', name='Leather bracers', description='Leather bracers', protection_value=2)


# Legs armor
light_boots = Armor(type_='boots', name='Light boots', description='Light boots', protection_value=1)
leather_boots = Armor(type_='boots', name='Leather boots', description='Leather boots', protection_value=2)
