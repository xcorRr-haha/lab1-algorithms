import random

def generate_sample(size_a=None, size_b=None, want_intersection=None):
    if size_a is None and size_b is None:
        size_b = random.randint(1, 10)
        size_a = size_b
    elif size_a is None:
        size_a = size_b
    elif size_b is None:
        size_b = size_a

    if want_intersection is None:
        want_intersection = random.choice([True, False])

    arr_a = [2 * int(i * size_b / size_a) + 1 for i in range(size_a)]
    arr_b = [2 * i for i in range(size_b)]

    if want_intersection and size_a > 0 and size_b > 0:
        pos_a = random.randint(0, size_a - 1)
        pos_b = random.randint(0, size_b - 1)
        arr_a[pos_a] = arr_b[pos_b]
        arr_a.sort()

    return arr_a, arr_b, bool(want_intersection)