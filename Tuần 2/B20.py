def book_allocation(p: list[int], m: int) -> int:
    n = len(p)
    if m > n:
        return -1
    def can_allocate(max_pages: int) -> bool:
        students_count = 1
        current_pages = 0
        for pages in p:
            if current_pages + pages > max_pages:
                students_count += 1
                current_pages = pages
                if students_count > m:
                    return False
            else:
                current_pages += pages
        return True
    low = max(p)
    high = sum(p)
    ans = high
    while low <= high:
        mid = (low + high) // 2
        if can_allocate(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1  
    return ans
