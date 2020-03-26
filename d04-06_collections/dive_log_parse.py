from collections import defaultdict, namedtuple, Counter
import csv

divelog_data = "divelog_21032020.csv"
Dive = namedtuple("Dive", "date dive_area area duration max_depth buddies remarks")

def get_dive_data(data=divelog_data):
    buddy_dict = defaultdict(list)
    dive_area_dict = defaultdict(list)
    with open(data, encoding="utf-8") as f:
        for line in csv.DictReader(f):
            date = line['date']
            dive_area = line['dive_area']
            area = line['area']
            duration = line['duration']
            max_depth = line['max_depth']
            buddies = line['buddies']
            remarks = line['remarks']
            d = Dive(date=date, dive_area=dive_area, area=area, duration=duration, max_depth=max_depth, buddies=buddies, remarks=remarks)
            buddy_list = [buddy.strip() for buddy in buddies.split(',')]
            for buddy in buddy_list:
                buddy_dict[buddy].append(d)
            dive_area_dict[dive_area].append(d)
    return buddy_dict, dive_area_dict

def find_most_common_in_dict(dict, common_num = 10):
    dict_cnt = Counter()
    for key, items in dict.items():
        dict_cnt[key] += len(items)
    return dict_cnt.most_common((common_num))


if __name__ == "__main__":
    buddy_dict, dive_area_dict = get_dive_data()
    print(find_most_common_in_dict(buddy_dict))
    print(find_most_common_in_dict(dive_area_dict))

