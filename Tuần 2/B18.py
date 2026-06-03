def find_kth_positive(a: list[int], k: int) -> int:
    low, high = 0, len(a) - 1
    while low <= high:
        mid = (low + high) // 2
        missing = a[mid] - (mid + 1)
        if missing < k:
            low = mid + 1
        else:
            high = mid - 1
    return k + low
