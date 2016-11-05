import random


class MainMenu():
    print('[1]: New game\n[2]: Load game\n[3]: Save game\n[4]: Exit')

    def handler(self, cmd):
        if cmd == '1':
            self.new_game()
        elif cmd == '2':
            self.load_game()
        elif cmd == 3:
            self.save_game()
        elif cmd == '4':
            exit()

    def new_game(self):
        print('IntroIntroIntro')
        name = input('Enter your name: ')
        protagonist = Character().create_protagonist(name)
        enemy = Character().create_enemy('Knight1')
        protagonist, enemy = Battle(protagonist, enemy).battle()

    def load_game(self):
        pass

    def save_game(self):
        pass


class Battle():
    def __init__(self, protagonist, enemy):
        self.protagonist = protagonist
        self.enemy = enemy

    def battle_info(self):
        print('{}{} {:>20}{}\n {:>36}{}\n'.format('Enemy health: ', self.enemy['health'],
                                                  'Your health: ', self.protagonist['health'],
                                                  'Your energy: ', self.protagonist['energy']))

    def enemy_attack(self):
        cmd = random.choice(['1', '2', '3'])

        if cmd == '1':
            print('{} has hit you to the head!'.format(self.enemy['name']))
            self.protagonist['health'] -= 50
            self.enemy['energy'] -= 30
        elif cmd == '2':
            print('{} has hit you to the body!'.format(self.enemy['name']))
            self.protagonist['health'] -= 30
            self.enemy['energy'] -= 25
        elif cmd == '3':
            print('{} has hit you to the legs!'.format(self.enemy['name']))
            self.protagonist['health'] -= 20
            self.enemy['energy'] -= 15

        return self.enemy, self.protagonist

    def battle(self):
        print('\nBattle is running!')
        self.battle_info()
        while self.enemy['health'] is not 0:
            print('[1]: Hit to the head (50 dmg/30 energy)\n'
                  '[2]: Hit to the body (30 dmg/25 energy)\n'
                  '[3]: Hit to the legs (20 dmg/15 energy)')
            cmd = input('Your choice: ')

            if cmd == '1':
                self.enemy['health'] -= 50
                self.protagonist['energy'] -= 30
                self.battle_info()
            elif cmd == '2':
                self.enemy['health'] -= 30
                self.protagonist['energy'] -= 25
                self.battle_info()
            elif cmd == '3':
                self.enemy['health'] -= 20
                self.protagonist['energy'] -= 15
                self.battle_info()

            if self.enemy['health'] is 0:
                print('You win')
                break
            elif self.protagonist['health'] is 0:
                print('You lose')
                break

            self.enemy, self.protagonist = self.enemy_attack()

        return self.protagonist, self.enemy


class City():
    print('You are in the city.\n'
          '[1]: Trader\n'
          '[2]: ')


class Character():
    def create_protagonist(self, name):
        protagonist = {'name': name, 'health': 100, 'energy': 100}
        return protagonist

    def create_enemy(self, name):
        enemy = {'name': name, 'health': 50, 'energy': 50}
        return enemy


main_menu = MainMenu()
main_menu.handler(input('Make your choice: '))
