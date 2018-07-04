import items


class Character:
    def __init__(self, name=None, health=None, energy=None, gold=None, exp=None, level=None):
        self.name = name
        self.health = health
        self.energy = energy
        self.gold = gold
        self.exp = exp
        self.level = level
        self.max_health = health
        self.max_energy = energy
        self.inventory = []

    def create_name(self):
        while True:
            name = input('Enter hero name.\nName length must be less than 20 symbols: ')

            if len(name) != 0 and len(name) <= 20:
                self.name = name
                break
            else:
                print('Try again')

    def display_stats(self):
        print('Name: {0} Level: {1}\n'
              'Health: {2} Experience: {3}\n'
              'Energy: {4} Gold: {5}\n'.format(self.name, self.level,
                                               self.health, self.exp,
                                               self.energy, self.gold))

    def show_inventory(self):
        for i, item in enumerate(self.inventory):
            print("%d: %s" % (i+1, item.name))

    def use_item(self):
        items_ids = []

        while True:
            if len(self.inventory) == 0:
                print("\nYou don't have any items\n")
                return 'Empty inventory'
            else:
                for i, item in enumerate(self.inventory):
                    items_ids.append(str(i+1))
                    print("[%d]: %s" % (i+1, item.name))

                cmd = input('Choose item: ')

                if cmd in items_ids:
                    item = self.inventory.pop(int(cmd)-1)

                    if isinstance(item, items.Food):
                        item.use(self)
                        break
                    elif isinstance(item, items.Potion):
                        if item.name == 'Health potion':
                            self.health += item.value

                            if self.health > self.max_health:
                                self.health = self.max_health

                            print('\n%s has healed health' % self.name)
                            break
                        elif item.name == 'Energy potion':
                            self.energy += item.value

                            if self.energy > self.max_energy:
                                self.energy = self.max_energy

                            print('\n%s has restored energy' % self.name)
                            break
                else:
                    print('Incorrect command\n')
