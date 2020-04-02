import random
import itertools
import sys
import time


def light():
    symbols = itertools.cycle(["Green", "Yellow", "Red"])
    while True:
        current_light = next(symbols)
        sys.stdout.write("\r" + current_light)
        if current_light == "Yellow":
            time.sleep(4)
        else:
            time.sleep(random.randint(15, 20))
        sys.stdout.flush()


if __name__ == "__main__":
    light()
