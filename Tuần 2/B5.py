def first_occurrence(a: list[int], x: int) -> int:
    low, high = 0, len(a) - 1
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if a[mid] == x:
            ans = mid
            high = mid - 1
        elif a[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return ans
def last_occurrence(a: list[int], x: int) -> int:
    low, high = 0, len(a) - 1
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if a[mid] == x:
            ans = mid
            low = mid + 1
        elif a[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return ans
def count_occurrences(a: list[int], x: int) -> int:
    first = first_occurrence(a, x)
    if first == -1:
        return 0
    last = last_occurrence(a, x)
    return last - first + 1