from utils import *


def _limit_health_value(hero):
    if hero.health > hero.max_health:
        hero.health = hero.max_health


def _heal(hero, heal_value, cost):
    if hero.health != hero.max_health:
        if hero.health < 0:
            hero.health = 0

        hero.health += heal_value
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

    commands = ['Smear a medicinal ointment (15 hp/ 5 gold)', 'Bandage the wounds (40 hp/ 10 gold)',
                'Take surgical care (150 hp/ 30 gold)', 'Back to the previous menu']

    while True:
        print('Your health: {0}/{1}\nYou have {2} gold'.format(hero.health, hero.max_health, hero.gold))
        display_commands(commands=commands)

        cmd = get_cmd()

        if cmd == '1':
            if _check_money(hero_money=hero.gold, cost=5):
                _heal(hero=hero, heal_value=15, cost=5)
                # TODO: move it into _heal function
                _limit_health_value(hero=hero)
            else:
                print("You don't have enough money")

        elif cmd == '2':
            if _check_money(hero_money=hero.gold, cost=10):
                _heal(hero=hero, heal_value=40, cost=10)
                _limit_health_value(hero=hero)
            else:
                print("You don't have enough money")
        elif cmd == '3':
            if _check_money(hero_money=hero.gold, cost=30):
                _heal(hero=hero, heal_value=150, cost=30)
                _limit_health_value(hero=hero)
            else:
                print("You don't have enough money")
        elif cmd == '4':
            return
        else:
            display_incorrect_command()
