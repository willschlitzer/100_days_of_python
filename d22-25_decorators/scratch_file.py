# How to write a decorate
from functools import wraps


def mydecorator(function):
    @wraps(function)
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

# args takes arbitrary number of arguments and treats it like a list
# kwargs takes key, value pairs and treats as dictionary