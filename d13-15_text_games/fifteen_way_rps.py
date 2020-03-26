from fifteen_way_rps_classes import Player, Roll
import random
from stat_reader import read_rolls, read_roll

BEST_OF = 3
results_dict = read_rolls()
roll_list = []
for key in results_dict.keys():
    roll_list.append(key)


def main():
    print("Time for some 15-way Rock, Paper Scissors!")
    print()
    player_name = input("What is your name?: ")
    game_loop(player_name=player_name)


def game_loop(player_name):
    computer_player = Player("Compy")
    human_player = Player(player_name)
    game_ongoing = True
    to_win = BEST_OF / 2
    while game_ongoing:
        print()
        print(
            "Score: {} {} : Computer {}".format(
                human_player.name, human_player.score, computer_player.score
            )
        )
        print()
        valid_roll = True
        for i, roll in enumerate(roll_list):
            print(i, roll)
        player_roll_index = int(input("Type the number next to your choice: "))
        try:
            player_roll = roll_list[player_roll_index]
        except:
            print("Not a valid roll")
            valid_roll = False
        if valid_roll:
            wins = results_dict[player_roll][0]
            losses = results_dict[player_roll][1]
            roll = Roll(player_roll, wins, losses)
            computer_roll = random.choice(roll_list)
            if computer_roll == roll.roll_name:
                print("You both rolled {}".format(computer_roll))
            elif computer_roll in roll.wins:
                print(
                    "Your {} beat the computer's {}".format(
                        roll.roll_name, computer_roll
                    )
                )
                human_player.score += 1
            elif computer_roll in roll.losses:
                print(
                    "Your {} lost to the computer's {}".format(
                        roll.roll_name, computer_roll
                    )
                )
                computer_player.score += 1
            if computer_player.score > to_win:
                print()
                print("The computer wins! Better luck next time")
                game_ongoing = False
            elif human_player.score > to_win:
                print()
                print("You win! Congratulations {}!".format(human_player.name))
                game_ongoing = False
    again = input("Play again? y/n ")
    if again.lower() == "y":
        game_loop(player_name=player_name)


if __name__ == "__main__":
    main()
