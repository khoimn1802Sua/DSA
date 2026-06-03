def binary_search(a: list[int], x: int) -> int:
    low, high = 0, len(a) - 1 
    while low <= high:
        mid = (low + high) // 2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            low = mid + 1
        else:
            high = mid - 1      
    return -1