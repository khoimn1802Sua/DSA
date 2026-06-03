def find_peak_element(a: list[int]) -> int:
    low, high = 0, len(a) - 1
    while low < high:
        mid = (low + high) // 2
        if a[mid] < a[mid + 1]:
            low = mid + 1
        else:
            high = mid
    return low