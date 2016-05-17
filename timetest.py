import datetime

def time_test(func):
    def decorator(*args, **kwargs):
        start_time = datetime.datetime.now()
        func(*args, **kwargs)
        print(str(datetime.datetime.now() - start_time))
    return decorator