from collections import defaultdict, namedtuple, Counter, deque
from timeit import timeit
import random


def createNamedTuple():
    """Demonstrate the use of named tuples"""
    # First field is the subclass (in this case User)
    # Second field can either be multple strings or a single string with whitespace/commas inbetween names
    User = namedtuple("User", "name role")
    user = User(name="Will", role="coder")
    # print(user.name)
    # print(user.role)


def createDefaultDict():
    """Demonstrates how defaultdicts work around errors that would happen with standard dicts"""
    missions_flown = [
        ("will", 50),
        ("matt", 10),
        ("oliver", 200),
        ("will", 75),
        ("matt", 20),
        ("oliver", 300),
    ]
    # Using a for loop to append the values would cause errors as keys are duplicated
    # Default dicts allow for a default data type to be added (in this case, lists)
    missions = defaultdict(list)
    for name, mission in missions_flown:
        missions[name].append(mission)
    print(missions)

#def demoCounter():

# print(timeit("createNamedTuple()", setup="from __main__ import createNamedTuple", number=100))
createDefaultDict()
