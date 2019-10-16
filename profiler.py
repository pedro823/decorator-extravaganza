from functools import wraps
from time import process_time
import random

def profiled(f):

    @wraps(f)
    def profiled_f(*args, **kwargs):
        t_start = process_time()
        return_value = f(*args, **kwargs)
        t_end = process_time()

        print(f'Function {f.__name__} took {t_end - t_start}s')
        return return_value

    return profiled_f


@profiled
def big_sort(li: list) -> list:
    for i in range(len(li) - 1):
        for j in range(i, len(li)):
            if li[i] > li[j]:
                li[i], li[j] = li[j], li[i]
    return li

@profiled
def quick_sort(li: list) -> list:
    li.sort()
    return li


if __name__ == '__main__':
    random.shuffle = profiled(random.shuffle)

    BIG_LIST = list(range(10000))
    random.shuffle(BIG_LIST)
    BIG_LIST_COPY = list(BIG_LIST)

    big_sort(BIG_LIST)
    quick_sort(BIG_LIST_COPY)