from utils import *


def _limit_health_value(hero):
    if hero.health > hero.max_health:
        hero.health = hero.max_health


def _heal(hero, heal_valuse, cost):
    if hero.health != hero.max_health:
        hero.health += heal_valuse
        hero.gold -= cost
    else:
        print("You're healthy, go away!")


def _check_money(hero_money, cost):
    if hero_money >= cost:
        return True
    else:
        return False


def doctor(hero):
    display_title('Doctor')

    commands = ['Resume', 'Heal a little (15 hp/ 5 golds)', 'Bandage the wounds (40 hp/ 10 gold)',
                'Take medical care (150 hp/ 30 golds)']

    while True:
        print('Your health: {0}\nYou have {1} golds'.format(hero.health, hero.gold))
        display_commands(commands=commands)

        cmd = get_cmd()

        if cmd == '1':
            return
        elif cmd == '2':
            if _check_money(hero_money=hero.gold, cost=5):
                _heal(hero=hero, heal_valuse=15, cost=5)
                _limit_health_value(hero=hero)
            else:
                print("You don't have enough money")

        elif cmd == '3':
            if _check_money(hero_money=hero.gold, cost=10):
                _heal(hero=hero, heal_valuse=40, cost=10)
                _limit_health_value(hero=hero)
            else:
                print("You don't have enough money")

        elif cmd == '4':
            if _check_money(hero_money=hero.gold, cost=30):
                _heal(hero=hero, heal_valuse=150, cost=30)
                _limit_health_value(hero=hero)
            else:
                print("You don't have enough money")
        else:
            display_incorrect_command()
