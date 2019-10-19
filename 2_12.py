# Write a decorator that takes a list of stop words and replaces in them
# with * inside decorated function


from functools import wraps


def stop_words(words: list):
    def decorator(func):
        @wraps(func)
        def wrapper(*args):
            return ' '.join([word if word not in words else '*'
                             for word in func(*args).strip('!').split(' ')]) + '!'
        return wrapper
    return decorator


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
