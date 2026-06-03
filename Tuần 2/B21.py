def split_array(a: list[int], k: int) -> int:
    def can_split(max_sum: int) -> bool:
        splits_count = 1
        current_sum = 0
        
        for num in a:
            if current_sum + num > max_sum:
                splits_count += 1
                current_sum = num
                if splits_count > k:
                    return False
            else:
                current_sum += num
        return True
    low = max(a)
    high = sum(a)
    ans = high
    while low <= high:
        mid = (low + high) // 2
        if can_split(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1   
    return ans
