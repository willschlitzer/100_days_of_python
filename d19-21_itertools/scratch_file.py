import itertools
import time
import sys

def spinner():
    symbols = itertools.cycle('-\|/')
    while True:
        sys.stdout.write('\r' + next(symbols))
        sys.stdout.flush()
        time.sleep(0.1)

def product():
    total_combos = 0
    for letter in itertools.product("schlitzer", repeat=4):
        print(letter)
        total_combos += 1
    print(total_combos)

def perm_com():
    people = "will nick nate".split()
    print(list(itertools.combinations(people, r=2)))
    print(list(itertools.permutations(people, r=3)))

if __name__ == "__main__":
    #spinner()
    #product()
    perm_com()