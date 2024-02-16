def debug(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"{func.__name__} called with {args}, {kwargs} returned {result}")
        return result
    return wrapper
