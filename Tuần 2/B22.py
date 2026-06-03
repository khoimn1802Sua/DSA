def find_median_sorted_arrays(a: list[int], b: list[int]) -> float:
    A, B = a, b
    m, n = len(A), len(B)
    if m > n:
        A, B = B, A
        m, n = n, m
    low, high = 0, m
    half_len = (m + n + 1) // 2
    while low <= high:
        i = (low + high) // 2
        j = half_len - i
        A_left = A[i - 1] if i > 0 else float('-inf')
        A_right = A[i] if i < m else float('inf')
        B_left = B[j - 1] if j > 0 else float('-inf')
        B_right = B[j] if j < n else float('inf')
        if A_left <= B_right and B_left <= A_right:
            if (m + n) % 2 == 1:
                return float(max(A_left, B_left))
            else:
                return (max(A_left, B_left) + min(A_right, B_right)) / 2.0
        elif A_left > B_right:
            high = i - 1
        else:
            low = i + 1  
    raise ValueError("Mảng đầu vào chưa được sắp xếp hoặc không hợp lệ")
