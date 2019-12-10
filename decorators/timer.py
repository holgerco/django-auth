import time


def timeit(function):
    def timed(*args, **kwargs):
        ts = time.time()
        result = function(*args, **kwargs)
        te = time.time()
        print('%r (%r, %r) %2.2f sec' % (function.__name__, args, kwargs, te - ts))
        return result

    return timed
