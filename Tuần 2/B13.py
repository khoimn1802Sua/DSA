def single_non_duplicate(a: list[int]) -> int:
    low, high = 0, len(a) - 1
    while low < high:
        mid = (low + high) // 2
        if mid % 2 == 1:
            mid -= 1
        if a[mid] == a[mid + 1]:
            low = mid + 2
        else:
            high = mid        
    return a[low]