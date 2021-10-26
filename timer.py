import time
from datetime import timedelta
from functools import wraps


def timer(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        print(f"Elapsed: {f.__name__} => {timedelta(seconds=time.time() - start)}")
        return result
    return wrapper
