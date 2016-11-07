import random


class StartGame():

    def main_menu(self):
        print('[1]: New game\n[2]: Load game\n[3]: Save game\n[4]: Exit')
        cmd = input('Make your choice: ')

        if cmd == '1':
            hero = self.new_game()
            return hero
        elif cmd == '2':
            self.load_game()
        elif cmd == '3':
            self.save_game()
        elif cmd == '4':
            exit()

    def new_game(self):
        name = input('Enter your name: ')
        hero = Character().create_character(name, 100, 100)
        enemy = Character().create_character('Knight_1', 60, 50)

        hero = Game().battle(hero, enemy)

        return hero

    def load_game(self):
        pass

    def save_game(self):
        pass


class Game():

    def battle(self, hero, enemy):
        print('\n{:>28}\n{:>17} {:>2} {:>3}'.format('BATTLE IS RUNNING', hero['name'], 'VS', enemy['name']))
        self.battle_info(hero, enemy)
        battle = True

        while battle:
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

            battle = self.is_game_over(battle, hero, enemy)
            if battle is False:
                break

            hero, enemy = self.enemy_attack(hero, enemy)

        return hero

    def enemy_attack(self, hero, enemy):
        cmd = random.choice(['1', '2', '3'])

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

    def is_game_over(self, battle_flag, hero, enemy):
        if hero['health'] <= 0:
            battle_flag = False
            print('{:>22}'.format('YOU LOSE'))
        elif enemy['health'] <= 0:
            print('{:>22}'.format('YOU WIN'))
            battle_flag = False

        return battle_flag


class City():
    def __init__(self, hero):
        self.hero = hero

    def menu(self):
        print('\n{:>28}'.format("You're in the city"))
        print('[1]: Main menu\n[2]: Trader\n[3]: Armory\n[4]: Blacksmith\n[5]: Arena')
        cmd = input('Make your choice: ')

        if cmd == '1':
            print('\n')
            StartGame().main_menu()
        elif cmd == '2':
            self.trader()
        elif cmd == '3':
            self.armory()
        elif cmd == '4':
            self.blacksmith()
        elif cmd == '5':
            pass

    def trader(self, hero):
        pass

    def armory(self, hero):
        pass

    def blacksmith(self, hero):
        pass


class Character():
    def create_character(self, name, health, energy):
        character = {'name': name, 'health': health, 'energy': energy}

        return character

hero = StartGame().main_menu()
City(hero).menu()
