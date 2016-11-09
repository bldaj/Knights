import random
import pickle


class StartGame():
    def __init__(self, hero=None):
        self.hero = hero

    def main_menu(self):
        print('[1]: New game\n'
              '[2]: Load game\n'
              '[3]: Save game\n'
              '[4]: Exit')
        cmd = input('Make your choice: ')

        if cmd == '1':
            hero = self.new_game()
            return hero
        elif cmd == '2':
            hero = self.load_game()
            return hero
        elif cmd == '3':
            self.save_game(self.hero)
        elif cmd == '4':
            exit()

    def new_game(self):
        name = input('Enter your name: ')
        hero = Character().create_character(name, 100, 100, 0, 100)
        enemy = Character().create_character('Knight_1', 60, 50, 100, 20)

        hero = Game().battle(hero, enemy)

        return hero

    def load_game(self):
        save = open('save.txt', 'rb')
        return pickle.load(save)

    def save_game(self, character):
        save = open('save.txt', 'wb')
        pickle.dump(character, save)
        save.close()


class Game():

    def battle(self, hero, enemy):
        print('\n{:>28}\n{:>17} {:>2} {:>3}'.format('BATTLE IS RUNNING', hero['name'], 'VS', enemy['name']))
        self.battle_info(hero, enemy)
        winner = ''

        while True:
            print('[1]: Hit to the head (50 dmg/30 energy)\n'
                  '[2]: Hit to the body (30 dmg/25 energy)\n'
                  '[3]: Hit to the legs (20 dmg/15 energy)')
            cmd = input('Your choice: ')

            if cmd == '1':
                enemy['health'] -= 50
                hero['energy'] -= 30
            elif cmd == '2':
                enemy['health'] -= 30
                hero['energy'] -= 25
            elif cmd == '3':
                enemy['health'] -= 20
                hero['energy'] -= 15

            winner = self.determine_winner(winner, hero, enemy)
            if winner is hero['name']:
                hero['exp'] += enemy['exp']
                hero['gold'] += enemy['gold']
                print('{:>22}'.format('YOU WIN'))
                break
            elif winner is enemy['name']:
                print('{:>22}'.format('YOU LOSE'))
                break

            hero, enemy = self.enemy_attack(hero, enemy)

        return hero

    def enemy_attack(self, hero, enemy):
        cmd = random.choice(['1'])

        if cmd == '1':
            print('\n{} has hit you to the head!\n'.format(enemy['name']))
            hero['health'] -= 50
            enemy['energy'] -= 30
            self.battle_info(hero, enemy)
        elif cmd == '2':
            print('\n{} has hit you to the body!\n'.format(enemy['name']))
            hero['health'] -= 30
            enemy['energy'] -= 25
            self.battle_info(hero, enemy)
        elif cmd == '3':
            print('\n{} has hit you to the legs!\n'.format(enemy['name']))
            hero['health'] -= 20
            enemy['energy'] -= 15
            self.battle_info(hero, enemy)

        return hero, enemy

    def battle_info(self, hero, enemy):
        print('{}{} {:>20}{}\n {:>36}{}\n'.format('Enemy health: ', enemy['health'],
                                                  'Your health: ', hero['health'],
                                                  'Your energy: ', hero['energy']))

    def determine_winner(self, winner, hero, enemy):
        if hero['health'] <= 0:
            winner = '{}'.format(enemy['name'])
        elif enemy['health'] <= 0:
            winner = '{}'.format(hero['name'])

        return winner


class City():
    def __init__(self, hero):
        self.hero = hero

    def menu(self):
        print('\n{:>28}'.format("You're in the city"))
        print('[1]: Main menu\n'
              '[2]: Info\n'
              '[3]: Trader\n'
              '[4]: Armory\n'
              '[5]: Blacksmith\n'
              '[6]: Arena')
        cmd = input('Make your choice: ')

        if cmd == '1':
            print('\n')
            self.hero = StartGame(self.hero).main_menu()
        elif cmd == '2':
            Character().info(hero)
        elif cmd == '3':
            self.trader()
        elif cmd == '4':
            self.armory()
        elif cmd == '5':
            self.blacksmith()
        elif cmd == '6':
            pass

    def trader(self, hero):
        pass

    def armory(self, hero):
        pass

    def blacksmith(self, hero):
        pass


class Character():
    def create_character(self, name, health, energy, exp, gold):
        character = {'name': name, 'health': health, 'energy': energy,
                     'exp': exp, 'gold': gold}

        return character

    def info(self, character):
        print(character)

hero = StartGame().main_menu()
City(hero).menu()
