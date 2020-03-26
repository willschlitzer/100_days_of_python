import csv


def read_rolls():
    with open("battle-table.csv") as fin:
        reader = csv.DictReader(fin)
        result_dict = {}
        for row in reader:
            name, wins, losses = read_roll(row)
            result_dict[name] = [wins, losses]
        return result_dict


def read_roll(row: dict):
    name = row["Attacker"]
    del row["Attacker"]
    del row[name]
    wins = []
    losses = []
    # print("Roll: {}".format(name))
    for k in row.keys():
        result = row[k].strip().lower()
        # can_defeat = row[k].strip().lower() == 'win'
        # print(" * {} will defeat {}? {}".format(name, k, can_defeat))
        if result == "win":
            wins.append(k.lower())
        else:
            losses.append(k.lower())
    return name.lower(), wins, losses


read_rolls()
