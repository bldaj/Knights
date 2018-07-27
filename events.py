from random import randint


def find_money(hero):
    gold_value = randint(1, 5)
    print('You was roaming around the Town when he found {1} gold'.format(hero.name, gold_value))

    hero.gold += gold_value


def sacrifice_the_poor(hero):
    if hero.gold > 0:
        gold_value = randint(1, 5)

        if gold_value > hero.gold:
            gold_value = hero.gold

        print('You sacrificed the poor {1} gold'.format(hero.name, gold_value))

        hero.gold -= gold_value
    else:
        gold_value = randint(1, 3)
        print('The beggar took pity on you and gave you {0} gold'.format(gold_value))

        hero.gold += gold_value



