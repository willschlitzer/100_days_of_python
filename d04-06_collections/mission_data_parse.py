from collections import defaultdict, namedtuple, Counter
import csv

mission_data = "apollo_data.csv"
Mission = namedtuple("Mission", "name start end lunar_orbit lunar_landing")


def get_mission_data(data=mission_data):
    astro_dict = defaultdict(list)
    with open(data, encoding="utf-8") as f:
        for line in csv.DictReader(f):
            name = line["name"]
            start = line["start_date"]
            end = line["end_date"]
            lunar_orbit = bool(line["lunar_orbit"])
            lunar_landing = bool(line["lunar_landing"])
            m = Mission(
                name=name,
                start=start,
                end=end,
                lunar_orbit=lunar_orbit,
                lunar_landing=lunar_landing,
            )
            for member in line["crew"].split(","):
                astro_dict[member].append(m)
    return astro_dict


if __name__ == "__main__":
    astro_data = get_mission_data()
    msn_cnt = Counter()
    for astro, mission in astro_data.items():
        msn_cnt[astro] += len(mission)
    print(msn_cnt.most_common())
