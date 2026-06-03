def search_rotated_array(a: list[int], x: int) -> int:
    low, high = 0, len(a) - 1
    while low <= high:
        mid = (low + high) // 2
        if a[mid] == x:
            return mid
        if a[low] <= a[mid]:
            if a[low] <= x < a[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if a[mid] < x <= a[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1