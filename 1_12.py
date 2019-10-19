# Write a decorator that prints a function with arguments passed to it.
# NOTE! It should print the function, not the result of its execution!
# For example:
#   "add called with 4, 5"


from functools import wraps


def logger(func):
    @wraps(func)
    def wrapper(*args):
        print(f'{func.__name__} called with arguments',
              ', '.join([str(arg) for arg in args]))
    return wrapper


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


add(4, 5)
square_all(1, 2, 45)