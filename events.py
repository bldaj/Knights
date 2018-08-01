from random import randint


def find_money(hero):
    gold_value = randint(1, 5)
    print('You were roaming around the Town when you found {1} gold'.format(hero.name, gold_value))

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


def hear_the_whisper():
    print('You were walking a lane when when you heard the whisper: "All our Gods have abandoned us..."')


def go_to_run(hero):
    print('You went to run.\nYou increased strength for 1 point')
    # TODO: use increase strength method
    # hero.strength += 1


