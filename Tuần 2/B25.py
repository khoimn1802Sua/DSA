def max_distance(x: list[int], m: int) -> int:
    x_sorted = sorted(x)  
    def can_place(min_force: int) -> bool:
        magnets_placed = 1
        last_position = x_sorted[0]
        for i in range(1, len(x_sorted)):
            if x_sorted[i] - last_position >= min_force:
                magnets_placed += 1
                last_position = x_sorted[i]
                if magnets_placed >= m:
                    return True
        return False
    low = 1
    high = x_sorted[-1] - x_sorted[0]
    ans = 1   
    while low <= high:
        mid = (low + high) // 2
        if can_place(mid):
            ans = mid
            low = mid + 1   
        else:
            high = mid - 1  
    return ans
