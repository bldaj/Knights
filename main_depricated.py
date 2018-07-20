import pickle
from random import choice

import items
from utils import *
from levels import levels
from enemies import enemies
from character import Character


def main_menu(hero=None):
    print_title('Main Menu')
    commands = ["New game", "Load game", "Save game", "Exit game"]

    show_commands(commands)

    cmd = input('Make your choice: ')

    if cmd == '1':
        hero = new_game()
        return hero
    elif cmd == '2':
        hero = load_game()
        return hero
    elif cmd == '3':
        save_game(hero)
    elif cmd == '4':
        exit('Complete game')
    else:
        print_incorrect_command()
        main_menu()

    if hero is not None:
        return hero


def new_game():
    print('\nVERY GREATEST STORY...and his name is...')
    name = ''

    while name == '':
        name = input("Enter hero's name: ")

    hero = Character(name, 100, 100, 0, 0, '1', max_health=100, max_energy=100)
    hero.tutorial = False    # it means that tutorial is not solved
    return hero


def load_game():
    with open('save.pickle', 'rb') as f1:
        hero = pickle.load(f1)
    with open('enemies.pickle', 'rb') as f2:
        global enemies
        enemies = pickle.load(f2)
    return hero


def save_game(hero):
    if hero is None:
        print("\nYou haven't hero to save\n")
        main_menu()
    else:
        with open('save.pickle', 'wb') as f1:
            pickle.dump(hero, f1)
        with open('enemies.pickle', 'wb') as f2:
            pickle.dump(enemies, f2)


def battle(hero, enemy):
    enemy_context = {'name': enemy.name, 'health': enemy.health,
                     'energy': enemy.energy, 'gold': enemy.gold,
                     'exp': enemy.exp}

    print('\n{:^40}\n{:>17} VS {}\n'.format('Battle Is Running', hero.name, enemy.name))

    while True:
        characters_info(hero, enemy)

        # hero will first attack and then will check is hero winner
        hero, enemy = hero_action(hero, enemy)

        # checking is hero win
        if who_is_winner(hero, enemy) == 'Hero':
            print('\n{:^40}'.format("You're a winner"))
            hero.exp += enemy.exp
            hero.gold += enemy.gold
            hero = level_up(hero)
            enemies.remove(enemy)
            break

        # then enemy will attack and then will check is enemy winner
        hero, enemy = enemy_action(hero, enemy)

        if who_is_winner(hero, enemy) == 'Enemy':
            return_enemy_context(enemy, enemy_context)
            print('\n{:^40}'.format("You're a loser"))
            break

    return hero


def hero_action(hero, enemy):
    print('[1]: To hit in head (40 dmg/20 energy)\n'
          '[2]: To hit in body (30 dmg/15 energy)\n'
          '[3]: To hit in legs (20 dmg/15 energy)\n'
          '[4]: Use item (5 energy)')

    cmd = input('Make your choice: ')

    if cmd == '1':
        enemy.health -= 40
        hero.energy -= 20
    elif cmd == '2':
        enemy.health -= 30
        hero.energy -= 15
    elif cmd == '3':
        enemy.health -= 20
        hero.energy -= 15
    elif cmd == '4':
        status = hero.use_item()

        if status == 'Empty inventory':
            pass
        else:
            hero.energy -= 5
            characters_info(hero, enemy)

        hero_action(hero, enemy)
    else:
        print_incorrect_command()
        hero_action(hero, enemy)

    return hero, enemy


def enemy_action(hero, enemy):
    cmd = choice([1, 2, 3])

    if cmd == 1:
        hero.health -= 40
        enemy.energy -= 20
        print('\n{} has hit you in head\n'.format(enemy.name))
    elif cmd == 2:
        hero.health -= 30
        enemy.energy -= 15
        print('\n{} has hit you in body\n'.format(enemy.name))
    elif cmd == 3:
        hero.health -= 20
        enemy.energy -= 15
        print('\n{} has hit you in legs\n'.format(enemy.name))

    return hero, enemy


def return_enemy_context(enemy, context):
    enemy.name = context['name']
    enemy.health = context['health']
    enemy.energy = context['energy']
    enemy.gold = context['gold']
    enemy.exp = context['gold']

    return enemy


def who_is_winner(hero, enemy):
    if enemy.health <= 0:
        return 'Hero'
    elif hero.health <= 0:
        return 'Enemy'


def characters_info(hero, enemy):
    print('{0}: {1} {4:>20}: {5}\n{2}: {3}\n'.format('Your health', hero.health, 'Your energy', hero.energy,
                                                     'Enemy health', enemy.health))


def choose_enemy():
    for i, enemy in enumerate(enemies):
        print('%d: %s' % (i+1, enemy.name))

    while True:
        try:
            cmd = int(input('Make your choice: '))
            return enemies[cmd-1]
        except ValueError:
            print_incorrect_command()
        except IndexError:
            print_incorrect_command()

def level_up(hero):
    exp = hero.exp

    for i in range(2, 13):
        if exp >= levels[str(i)] and exp < levels[str(i+1)]:
            print('\n{:^40}'.format("LEVEL UP"))

            hero.level = str(i)
            hero.max_health += 10
            hero.max_energy += 10
            hero.health = hero.max_health
            hero.energy += hero.max_energy
            break

    return hero


def show_info(hero):
    print_title('Stats')
    print('Name: {0} Level: {1}\n'
          'Health: {2} Experience: {3}\n'
          'Energy: {4} Gold: {5}\n'.format(hero.name, hero.level,
                                           hero.health, hero.exp,
                                           hero.energy, hero.gold))


def tutorial(hero):
    battle_description = "\nIt's battle place, my hero! You should use command like in the main menu I mean 1, 2, 3.\n" \
                         "So, you have health and energy. Health you know why, energy - allows you to use your skills.\n" \
                         "The battle takes step by step. You'll see information about your hero after any step. " \
                         "Also, you'll get exp and gold.\n" \
                         "Exp allows you to get new level, gold you can spend in a town.\n"

    town_description = "\nWelcome to the Town!\n" \
                       "After each battle you will get here. The Town might you to call the main menu, to upgrade your\n" \
                       "hero at blacksmith, to buy and sell some things, to show your characteristics and of course from\n" \
                       "here you can go to the new battle."

    dummy = enemies[0]

    print(battle_description)
    input("If you're ready press [enter]...")

    hero = battle(hero, dummy)

    print(town_description)

    hero.tutorial = True    # it sets flag that mean tutorial is solved

    return hero


class Town:
    def __init__(self, hero):
        self.hero = hero

    def menu(self):
        print_title("Now you're in the Town")

        commands = ["Main menu", "Hero's information", "Hero's inventory", "Trader", "Blacksmith", "Doctor",
                    "To the Arena"]

        while True:
            show_commands(commands)

            cmd = input('\nMake your choice: ')

            if cmd == '1':
                self.hero = main_menu(self.hero)
            elif cmd == '2':
                show_info(self.hero)
            elif cmd == '3':
                self.hero.show_inventory()
                print('\n')
            elif cmd == '4':
                self.trader(self.hero)
            elif cmd == '5':
                self.blacksmith()
            elif cmd == '6':
                self.hero = self.doctor(self.hero)
            elif cmd == '7':
                enemy = choose_enemy()
                self.hero = battle(self.hero, enemy)
            else:
                print_incorrect_command()
                self.menu()

    def doctor(self, hero):
        commands = ["Heal 30 health (5 gold)", "Heal 50 health (10 gold)",
                    "Heal 100 health (20 gold)", "Return to Town"]

        print('Your health: %d\n'
              'Your gold: %d\n' % (hero.health, hero.gold))

        show_commands(commands)

        cmd = input('\nMake your choice: ')

        if cmd == '1':
            hero.gold -= 5
            hero.health += 30
        elif cmd == '2':
            hero.gold -= 10
            hero.health += 50
        elif cmd == '3':
            hero.gold -= 20
            hero.health += 100
        elif cmd == '4':
            self.menu()
        else:
            print_incorrect_command()
            self.doctor(hero)

        if hero.health > hero.max_health:
            hero.health = hero.max_health

        return hero

    def trader(self, hero):
        print_title('Trader')
        print('Do you want to buy or sell something, adventurer?')
        print('[1]: Buy\n'
              '[2]: Sell\n'
              '[3]: Return to Town')

        cmd = input('Make your choice: ')

        if cmd == '1':
            item_ids = []

            for i, item in enumerate(trader):
                item_ids.append(str(i+1))
                print('[%d]: %s' % (i+1, item.name))
            print('To exit press [enter]\n')

            cmd = input('Make your choice: ')

            if cmd in item_ids:
                int_cmd = int(cmd)-1
                hero.inventory.append(trader[int_cmd])
                hero.gold -= trader[int_cmd].cost

                print("You bought %s\n" % trader[int_cmd].name)
        elif cmd == '2':
            item_ids = []

            for i, item in enumerate(hero.inventory):
                item_ids.append(str(i+1))
                print('[%d]: %s' % (i+1, item.name))
            print('\n')

            cmd = input('Make your choice: ')

            if cmd in item_ids:
                int_cmd = int(cmd)-1
                hero.gold += hero.inventory[int_cmd].cost
                print('You sold %s' % hero.inventory[int_cmd].name)
                hero.inventory.pop(int_cmd)
        elif cmd == '3':
            self.menu()
        else:
            print_incorrect_command()
            self.trader(hero)

    def blacksmith(self):
        pass


def run_game():
    hero = main_menu()

    if hero.tutorial is not True:
        hero = tutorial(hero)

    Town(hero).menu()


enemies = enemies
trader = items.trader


if __name__ == '__main__':
    run_game()
