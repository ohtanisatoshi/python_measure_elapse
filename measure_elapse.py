import time
from functools import wraps

def measure_elapse(fn):
    @wraps(fn)
    def measure_time(*args, **kwargs):
        t1 = time.time()
        result = fn(*args, **kwargs)
        t2 = time.time()
        print('@timefn: {} took {:.4f} seconds'.format(fn.__name__, (t2-t1)))
        return result
    return measure_time

def main():
    pass


if __name__ == '__main__':
    main()
