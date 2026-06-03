def find_closest_elements(a: list[int], k: int, x: int) -> list[int]:
    low, high = 0, len(a) - k
    while low < high:
        mid = (low + high) // 2
        if x - a[mid] > a[mid + k] - x:
            low = mid + 1
        else:
            high = mid
    return a[low:low + k]
