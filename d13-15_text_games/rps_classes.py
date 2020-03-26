class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_win(self):
        self.score += 1


class Roll:
    def __init__(self, roll_name):
        self.roll_name = roll_name
        if roll_name == "rock":
            self.loses = "paper"
            self.wins = "scissors"
        elif roll_name == "paper":
            self.loses = "scissors"
            self.wins = "rock"
        elif roll_name == "scissors":
            self.loses = "rock"
            self.wins = "paper"
