from random import choice
import pickle


class Game():
    def main_menu(self, hero=None):
        print('[1]: New game\n'
              '[2]: Load game\n'
              '[3]: Save game\n'
              '[4]: Exit game')

        cmd = self.make_choice()

        if cmd == '1':
            hero = self.new_game()
            return hero
        elif cmd == '2':
            hero = self.load_game()
            return hero
        elif cmd == '3':
            self.save_game(hero)
        elif cmd == '4':
            exit('Completed games')
        else:
            print('\nIncorrect command')
            self.main_menu()

    def new_game(self):
        print('\nVERY GREATEST STORY...and his name is...')
        name = ''
        global MAX_HEALTH

        while name == '':
            name = input("Enter hero's name: ")

        hero = Character().create_character(name, MAX_HEALTH, 100, 0, 0, '1')
        hero['tutorial'] = False    # it means that tutorial is not solved
        return hero

    def load_game(self):
        with open('save.pickle', 'rb') as f:
            hero = pickle.load(f)
            return hero

    def save_game(self, hero):
        with open('save.pickle', 'wb') as f:
            pickle.dump(hero, f)

    def make_choice(self):
        cmd = input('Make your choice: ')
        return cmd

    def battle(self, hero, enemy):
        print('\n{:^40}\n{:>17} VS {}\n'.format('Battle Is Running', hero['name'], enemy['name']))

        while True:
            self.characters_info(hero, enemy)
            print('[1]: To hit in head (40 dmg/20 energy)\n'
                  '[2]: To hit in body (30 dmg/15 energy)\n'
                  '[3]: To hit in legs (20 dmg/15 energy)')

            hero, enemy = self.hero_attack(hero, enemy)
            if self.who_is_winner(hero, enemy) == 'Hero':
                print('\n{:^40}'.format("You're a winner"))
                hero['exp'] = enemy['exp']
                hero['gold'] = enemy['gold']
                hero = Character().level_up(hero)
                break

            hero, enemy = self.enemy_attack(hero, enemy)
            if self.who_is_winner(hero, enemy) == 'Enemy':
                print('\n{:^40}'.format("You're a loser"))
                break

        return hero

    def hero_attack(self, hero, enemy):
        cmd = self.make_choice()

        if cmd == '1':
            enemy['health'] -= 40
            hero['energy'] -= 20
        elif cmd == '2':
            enemy['health'] -= 30
            hero['energy'] -= 15
        elif cmd == '3':
            enemy['health'] -= 20
            hero['energy'] -= 15
        else:
            print('\nIncorrect command')
            self.hero_attack(hero, enemy)

        return hero, enemy

    def enemy_attack(self, hero, enemy):
        cmd = choice(['1', '2', '3'])

        if cmd == '1':
            hero['health'] -= 40
            enemy['energy'] -= 20
            print('\n{} has hit you in head\n'.format(enemy['name']))
        elif cmd == '2':
            hero['health'] -= 30
            enemy['energy'] -= 15
            print('\n{} has hit you in body\n'.format(enemy['name']))
        elif cmd == '3':
            hero['health'] -= 20
            enemy['energy'] -= 15
            print('\n{} has hit you in legs\n'.format(enemy['name']))

        return hero, enemy

    def characters_info(self, hero, enemy):
        print('{0}: {1} {4:>20}: {5}\n{2}: {3}\n'.format('Your health', hero['health'], 'Your energy', hero['energy'],
                                                         'Enemy health', enemy['health']))

    def who_is_winner(self, hero, enemy):
        if enemy['health'] <= 0:
            return 'Hero'
        elif hero['health'] <= 0:
            return 'Enemy'


class Character():
    global MAX_HEALTH
    MAX_HEALTH = 100

    def create_character(self, name, health, energy, gold, exp, level):
        character = {'name': name,
                     'health': health,
                     'energy': energy,
                     'gold': gold,
                     'exp': exp,
                     'level': level}

        return character

    def enemy_list(self):
        enemies = []

        names = ['Villager', 'Farmer', 'Knight']
        healths = [80, 100, 140]
        energies = [100, 100, 100]

        for i in range(3):
            enemy = self.create_character(names[i], healths[i], energies[i])
            enemies.append(enemy)

        return enemies

    def levels(self):
        levels = {'1': 0}   # Initialize first level
        exp = 300
        levels['2'] = exp   # 300 experience points need to get second level

        for i in range(3, 13):
            exp *= 1.3
            levels[str(i)] = int(exp)

        return levels

    def level_up(self, hero):
        levels = self.levels()
        exp = hero['exp']
        global MAX_HEALTH

        for i in range(2, 13):
            if exp >= levels[str(i)] and exp < levels[str(i+1)]:
                print('\n{:^40}'.format("LEVEL UP"))

                MAX_HEALTH += 10
                hero['level'] = str(i)
                hero['health'] = MAX_HEALTH
                hero['energy'] += 10
                break

        return hero

    def show_info(self, hero):
        print('\n{:^40}\n'.format('Information about your hero'))
        print('Name: {0} Level: {1}\n'
              'Health: {2} Experience: {3}\n'
              'Energy: {4} Gold: {5}\n'.format(hero['name'], hero['level'],
                                               hero['health'], hero['exp'],
                                               hero['energy'], hero['gold']))


class Town():
    def __init__(self, hero):
        self.hero = hero

    def menu(self):
        print("\n{:^40}\n".format("Now you're in the Town."))

        while True:
            print("[1]: Main menu\n"
                  "[2]: Hero's information\n"
                  "[3]: Trader\n"
                  "[4]: Blacksmith\n"
                  "[5]: To the Arena")

            cmd = Game().make_choice()

            if cmd == '1':
                Game().main_menu(self.hero)
            elif cmd == '2':
                Character().show_info(self.hero)
            elif cmd == '3':
                self.trader()
            elif cmd == '4':
                self.blacksmith()
            elif cmd == '5':
                pass
            else:
                print('\nIncorrect command')
                self.menu()

    def trader(self):
        pass

    def blacksmith(self):
        pass


class Tutorial():
    battle_description = "\nIt's battle place, my hero! You should use command like in the main menu I mean 1, 2, 3.\n" \
                         "So, you have health and energy. Health you know why, energy - might you to use your skills.\n" \
                         "The battle takes step by step. You'll see information about your hero after any step. " \
                         "Also, you'll get exp and gold.\n" \
                         "Exp allows you to get new level, gold you can spend in a town.\n"

    town_description = "\nWelcome to the Town!\n" \
                       "After each battle you will get here. The Town might you to call the main menu, to upgrade your " \
                       "hero at blacksmith, to buy and sell some things, to show your characteristics and of course from" \
                       "here you can go to the new battle."

    def run(self, hero):
        dummy = Character().create_character('Dummy', 60, 100, 100, 450, 1)

        print(self.battle_description)
        input("If you're ready press any key...")

        hero = Game().battle(hero, dummy)

        print(self.town_description)

        hero['tutorial'] = True    # it sets flag that mean tutorial is solved

        return hero


class RunGame():
    hero = Game().main_menu()

    if hero['tutorial'] is not True:
        hero = Tutorial().run(hero)

    Town(hero).menu()


RunGame()
