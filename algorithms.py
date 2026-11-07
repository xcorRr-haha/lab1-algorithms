def two_pointers(a, b):
    # O(M + N)
    if len(a) > len(b):
        a, b = b, a
        
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
    # O(min(M,N) * log(max(M,N)))
    if len(a) > len(b):
        a, b = b, a

    for element in a:
        low = 0
        high = len(b) - 1
        
        # Ручками, а не встроенными 
        while low <= high:
            mid = (low + high) // 2
            if b[mid] == element:
                return True
            elif b[mid] < element:
                low = mid + 1
            else:
                high = mid - 1
    return False

def exponential(a, b):
    # O(min(M,N) * log(2 * max(M,N) / min(M,N)))
    if len(a) > len(b):
        a, b = b, a
    
    b_len = len(b)
    b_idx = 0
    
    for element in a:
        if b_idx >= b_len:
            break
        if b[b_idx] == element:
            return True
        elif b[b_idx] > element:
            continue
        
        # прыгскок
        step = 1
        while b_idx + step < b_len and b[b_idx + step] < element:
            step *= 2
        
        # граничим
        low = b_idx + step // 2 - 1
        high = min(b_idx + step, b_len - 1) + 1

        # Ручками бинпоиском по отрезку
        while (high - low > 1):
            mid = (low + high) // 2
            if b[mid] == element:
                return True
            elif b[mid] > element:
                high = mid
            else:
                low = mid
                
        b_idx = high
    return False

def double_binary(a, b):
    # O(min(M,N) * log(2 * max(M,N) / min(M,N)))
    if len(a) > len(b):
        a, b = b, a

    def solve(start_a, end_a, start_b, end_b):
        if start_a > end_a or start_b > end_b:
            return False

        mid_a = (start_a + end_a) // 2
        target = a[mid_a]
        
        low = start_b
        high = end_b
        
        while low <= high:
            mid_b = (low + high) // 2
            if b[mid_b] == target:
                return True
            elif b[mid_b] < target:
                low = mid_b + 1
            else:
                high = mid_b - 1
                
        return (solve(start_a, mid_a - 1, start_b, high) or 
                solve(mid_a + 1, end_a, low, end_b))

    return solve(0, len(a) - 1, 0, len(b) - 1)