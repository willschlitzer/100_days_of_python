class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_win(self):
        self.score += 1


class Roll:
    def __init__(self, roll_name, wins, losses):
        self.roll_name = roll_name
        self.wins = wins
        self.losses = losses
