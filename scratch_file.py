from collections import defaultdict, namedtuple, Counter, deque
from timeit import timeit
import random

def createNamedTuple():
    """Demonstrate the user of named tuples"""
    # First field is the subclass (in this case User)
    # Second field can either be multple strings or a single string with whitespace/commas inbetween names
    User = namedtuple('User', 'name role')
    user = User(name="Will", role = "coder")
    #print(user.name)
    #print(user.role)


#print(timeit("createNamedTuple()", setup="from __main__ import createNamedTuple", number=100))

