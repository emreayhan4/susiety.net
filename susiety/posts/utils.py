import random


def random_name():
    with open('susiety/static/names/basic_list.txt') as f:
        names = f.read().splitlines()
        rname = random.choice(names)
    return rname
