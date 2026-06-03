def search_matrix(matrix: list[list[int]], x: int) -> bool:
    if not matrix or not matrix[0]:
        return False
    m, n = len(matrix), len(matrix[0])
    low, high = 0, m * n - 1
    while low <= high:
        mid = (low + high) // 2
        r, c = mid // n, mid % n
        val = matrix[r][c]
        if val == x:
            return True
        elif val < x:
            low = mid + 1
        else:
            high = mid - 1    
    return False