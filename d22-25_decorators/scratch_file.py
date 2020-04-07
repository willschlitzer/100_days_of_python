# How to write a decorate
from functools import wraps
import time

def mydecorator(function):
    @wraps(functions)
    def wrapper(*args, **kwargs):
        # do something before the original function is called
        # it's called the passed in function
        result = function(*args, **kwargs)
        # do something after function is called
        return result
    return wrapper

@mydecorator
def my_function(args):
    pass