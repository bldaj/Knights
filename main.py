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
        name = input('Enter your name: ')
        protagonist = CreateCharacter().protagonist(name)
        enemy = CreateCharacter().enemy('Knight 1')
        battle = Battle(protagonist, enemy)
        battle.battle()

    def load_game(self):
        pass

    def save_game(self):
        pass


class Battle():
    def __init__(self, protagonist, enemy):
        self.protagonist = protagonist
        self.enemy = enemy

    def battle(self):
        print('\nHello! Battle is running!')
        while self.enemy['health'] is not 0:
            print('[1]: Hit to the head\n[2]: Hit to the body\n[3]: Hit to the legs')
            cmd = input('Your choice: ')

            if cmd == '1':
                self.enemy['health'] -= 50
                self.protagonist['energy'] -= 30
                print('Enemy health: {0}\nYour energy: {1}\n'.format(self.enemy['health'],
                                                                     self.protagonist['energy']))
            elif cmd == '2':
                self.enemy['health'] -= 30
                self.protagonist['energy'] -= 25
                print('Enemy health: {0}\n Your energy: {1}\n'.format(self.enemy['health'],
                                                                      self.protagonist['energy']))
            elif cmd == '3':
                self.enemy['health'] -= 20
                self.protagonist['energy'] -= 15
                print('Enemy health: {0}\n Your energy: {1}\n'.format(self.enemy['health'],
                                                                      self.protagonist['energy']))

            if self.enemy['health'] is 0:
                print('You win')
        return self.protagonist, self.enemy


class CreateCharacter():
    def protagonist(self, name):
        protagonist = {'name': name, 'health': 100, 'energy': 100}
        return protagonist

    def enemy(self, name):
        enemy = {'name': name, 'health': 50, 'energy': 50}
        return enemy

main_menu = MainMenu()
main_menu.handler(input('Make your choice: '))
