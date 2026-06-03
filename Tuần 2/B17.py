
def ship_within_days(weights: list[int], days: int) -> int:
    def can_ship(capacity: int) -> bool:
        current_weight = 0
        required_days = 1
        for w in weights:
            if current_weight + w > capacity:
                required_days += 1
                current_weight = w
                if required_days > days:
                    return False
            else:
                current_weight += w
        return required_days <= days
    low = max(weights)
    high = sum(weights)
    ans = high
    while low <= high:
        mid = (low + high) // 2
        if can_ship(mid):
            ans = mid
            high = mid - 1 
        else:
            low = mid + 1   
    return ans
