def search_insert(a: list[int], x: int) -> int:
    low, high = 0, len(a) - 1
    ans = len(a)
    while low <= high:
        mid = (low + high) // 2
        if a[mid] >= x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans