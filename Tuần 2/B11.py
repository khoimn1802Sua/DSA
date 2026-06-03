def find_min_rotated_array(a: list[int]) -> int:
    if not a:
        raise ValueError("Mảng không được rỗng") 
    low, high = 0, len(a) - 1
    if a[low] <= a[high]:
        return a[low]
    while low < high:
        mid = (low + high) // 2
        if a[mid] > a[high]:
            low = mid + 1
        else:
            high = mid            
    return a[low]
