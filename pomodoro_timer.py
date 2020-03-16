from datetime import datetime, timedelta
from time import sleep


def run_timer():
    # The length of time assigned to a given task
    task_length = timedelta(minutes=25)
    start = datetime.today()
    pom_count = 0
    while True:
        elapsed = datetime.today() - start
        if elapsed >= task_length:
            pom_count = run_break(pom_count)
            start = datetime.today()
        else:
            if (elapsed.seconds % 60) == 0:
                remaining_time = int((task_length.seconds - elapsed.seconds) / 60)
                print(str(remaining_time) + " minutes remaining on your task!")
                sleep(50)


def run_break(pom_count):
    # The length of the short break
    short_break = timedelta(minutes=5)
    # The length of a long break
    long_break = timedelta(minutes=30)
    # How many pomodoros happen until a long break
    pom_nums = 4
    if pom_count >= pom_nums:
        break_length = long_break
        pom_count = 0
    else:
        break_length = short_break
        pom_count += 1

    break_start = datetime.today()
    print("Time for a break!")
    while True:
        break_elapsed = datetime.today() - break_start
        if break_elapsed >= break_length:
            print("Break's over")
            return pom_count
        else:
            if (break_elapsed.seconds % 60) == 0:
                break_remaining_time = int(
                    (break_length.seconds - break_elapsed.seconds) / 60
                )
                print(str(break_remaining_time) + " minutes remaining on your break!")
                sleep(50)


if __name__ == "__main__":
    run_timer()
