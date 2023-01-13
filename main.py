import time
from copy import deepcopy
from pprint import pprint


def time_of_function(function):
    def wrapped(*args, **kwargs):
        start_time = time.perf_counter_ns()
        res = function(*args, **kwargs)
        print(f'{time.perf_counter_ns() - start_time:,} наносекунд')
        return res

    return wrapped


@time_of_function
def drop_duplicates_dicts_1(lst: list[dict]):
    """Удаляет дубли, но не сохраняет порядок элементов возвращаемого списка."""
    s = set((frozenset(elem.items()) for elem in lst))
    return [dict(elem) for elem in s]


@time_of_function
def drop_duplicates_dicts_2(lst: list[dict]):
    """
    Удаляет дубли, и сохраняет порядок элементов возвращаемого списка.
    При этом сложность становится O(n^2)
    """
    s = tuple(frozenset(elem.items()) for elem in lst)
    new_list = []
    for elem in s:
        if elem not in new_list:
            new_list.append(elem)
    return [dict(elem) for elem in new_list]


def main():
    some_list = [
        {"key1": "value1"},
        {"k1": "v1", "k2": "v2", "k3": "v3"},
        {}, {},
        {"key1": "value1"},
        {"key1": "value1"},
        {"key2": "value2"},
    ] * 10000

    new_list = drop_duplicates_dicts_1(deepcopy(some_list))
    pprint(new_list)
    new_list = drop_duplicates_dicts_2(deepcopy(some_list))
    pprint(new_list)


if __name__ == '__main__':
    main()
