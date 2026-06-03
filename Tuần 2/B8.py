def integer_sqrt(n: int) -> int:
    if n < 2:
        return n
    low, high = 1, n
    ans = 0
    while low <= high:
        mid = (low + high) // 2
        if mid * mid == n:
            return mid
        elif mid * mid < n:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return ans
