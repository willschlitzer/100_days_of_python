from actors import Creature, Wizard, Dragon
import random

def main():
    print_title()
    game_loop()

def print_title():
    print("__________________________")
    print("    Wizard Game")
    print("__________________________")
    print()

def game_loop():
    creatures = [Creature("Bat", 5),
                 Creature("Toad", 1),
                 Creature("Tiger", 12),
                 Dragon("Dragon", 50, scaliness=2, breathes_fire = False),
                 Wizard("Evil Wizard", 100)]
    hero = Wizard('Gandolf', 75)
    while True:
        # randomly choose a creature
        active_creature = random.choice(creatures)
        print("A {} of level {} has appeared".format(active_creature.name, active_creature.level))
        cmd = input("Do you [a] attack, [r]unaway, or [l]ook around? ")
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
                print("{} defeated the {}!".format(hero.name, active_creature.name))
        elif cmd == 'r':
            print("{} flees!".format(hero.name))
        elif cmd == 'l':
            print("{} looks around and sees:".format(hero.name))
            for c in creature:
                print("* {} of level {}".format(c.name, c.level))
        else:
            print("Exiting game")
            break
        if not creatures:
            print("You've defeated all of the creatures")
            break



if __name__ == "__main__":
    main()