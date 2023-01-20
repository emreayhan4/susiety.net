import os
import random


def r_quotes():
    with open('susiety/static/quotes/quotes.txt',"r") as file:
        lines = file.read().splitlines()
        line = random.choice(lines)
    return line


def random_banner():
    direc = os.path.dirname(os.path.abspath(__file__))
    banner_img = random.choice(os.listdir(direc + '/static/banner'))
    return banner_img
