def min_eating_speed(piles: list[int], h: int) -> int:
    def can_eat_all(speed: int) -> bool:
        hours = 0
        for p in piles:
            hours += (p + speed - 1) // speed
            if hours > h:
                return False
        return hours <= h
    low = 1
    high = max(piles)
    ans = high
    while low <= high:
        mid = (low + high) // 2
        if can_eat_all(mid):
            ans = mid
            high = mid - 1  
        else:
            low = mid + 1  
    return ans
