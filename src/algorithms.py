import bisect

def two_pointers(a, b):
    idx_a = 0
    idx_b = 0
    while idx_a < len(a) and idx_b < len(b):
        if a[idx_a] == b[idx_b]:
            return True
        elif a[idx_a] < b[idx_b]:
            idx_a += 1
        else:
            idx_b += 1
    return False

def binary_search(a, b):
    for element in a:
        index = bisect.bisect_left(b, element)
        if index < len(b) and b[index] == element:
            return True
    return False

def exponential(a, b):
    b_len = len(b)
    for element in a:
        if b_len == 0 or element < b[0]:
            continue
        step = 1
        while step < b_len and b[step] < element:
            step *= 2
        start = step // 2
        end = min(step, b_len)
        index = bisect.bisect_left(b, element, start, end)
        if index < b_len and b[index] == element:
            return True
    return False

def double_binary(a, b):
    if not a or not b:
        return False
    middle = len(a) // 2
    target = a[middle]
    pos_in_b = bisect.bisect_left(b, target)
    if pos_in_b < len(b) and b[pos_in_b] == target:
        return True
    return (double_binary(a[:middle], b[:pos_in_b]) or 
            double_binary(a[middle+1:], b[pos_in_b:]))