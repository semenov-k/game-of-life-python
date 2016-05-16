import time

def time_test(func):
    def decorator(*args, **kwargs):
        start_time = time.clock()
        func(*args, **kwargs)
        print(str(time.clock() - start_time))
    return decorator