import random


class MainMenu():
    print('[1]: New game\n[2]: Load game\n[3]: Save game\n[4]: Exit')

    def handler(self, cmd):
        if cmd == '1':
            self.new_game()
        elif cmd == '2':
            self.load_game()
        elif cmd == '3':
            self.save_game()
        elif cmd == '4':
            exit()

    def new_game(self):
        name = input('Enter your name: ')
        protagonist = Character().create_protagonist(name)
        enemy = Character().create_enemy('Knight 1')
        protagonist = Battle(protagonist, enemy)
        protagonist.battle()

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
            print('{} has hit you to the head!\n'.format(self.enemy['name']))
            self.protagonist['health'] -= 50
            self.enemy['energy'] -= 30
            self.battle_info()
        elif cmd == '2':
            print('{} has hit you to the body!\n'.format(self.enemy['name']))
            self.protagonist['health'] -= 30
            self.enemy['energy'] -= 25
            self.battle_info()
        elif cmd == '3':
            print('{} has hit you to the legs!\n'.format(self.enemy['name']))
            self.protagonist['health'] -= 20
            self.enemy['energy'] -= 15
            self.battle_info()

        return self.enemy, self.protagonist

    def battle(self):
        print('\nBattle is running!')
        battle = True
        self.battle_info()

        while battle:
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

            battle = self.is_game_over(battle)
            if not battle:
                break

            self.enemy, self.protagonist = self.enemy_attack()

        return self.protagonist

    def is_game_over(self, battle_flag):
        if self.protagonist['health'] <= 0:
            battle_flag = False
            print('YOU LOSE')
        elif self.enemy['health'] <= 0:
            print('YOU WIN')
            battle_flag = False

        return battle_flag

class Character():
    def create_protagonist(self, name):
        protagonist = {'name': name, 'health': 100, 'energy': 100}
        return protagonist

    def create_enemy(self, name):
        enemy = {'name': name, 'health': 50, 'energy': 50}
        return enemy

main_menu = MainMenu()
main_menu.handler(input('Make your choice: '))
