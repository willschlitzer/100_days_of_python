from functools import wraps
import time

def timeit(func):
    """Decorator to time a functions"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("== Starting Timer ==")
        start = time.time()
        # Call the decorated function
        func(*args, **kwargs)
        end = time.time()
        print(f'== {func.__name__} took {int(end-start)} seconds to complete')
    return wrapper

@timeit
def generate_report():
    time.sleep(2)
    print('Report complete')

generate_report()