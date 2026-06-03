def exists(a: list[int], x: int) -> bool:
    low, high = 0, len(a) - 1 
    while low <= high:
        mid = (low + high) // 2
        if a[mid] == x:
            return True
        elif a[mid] < x:
            low = mid + 1
        else:
            high = mid - 1         
    return False
