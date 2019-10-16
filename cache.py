from functools import wraps

def cached(f):

    cache = {}
    def with_cache(*args, **kwargs):
        serialized_args = f'{args}:{kwargs}'
        cache_result = cache.get(serialized_args)

        if cache_result is not None:
            return cache_result

        value = f(*args, **kwargs)
        cache[serialized_args] = value

        # print(cache)
        return value

    return with_cache

@cached
def fibonacci(n):
    if n < 0:
        return -1
    
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(200))
print(fibonacci(400))
print(fibonacci(600))
