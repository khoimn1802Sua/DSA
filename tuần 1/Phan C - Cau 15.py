import math
def so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def tim_so_nguyen_to_dau_tien(a):
    for i in range(len(a)):
        if so_nguyen_to(a[i]):
            return a[i], i
    return -1, -1