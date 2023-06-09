import argparse

from ..Models.Units import Enemy

def enemy_generator(number: int):
    value = 0
    while value < number:
        yield Enemy(1)
        value +=1

# Work in Progress
