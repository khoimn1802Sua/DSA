def sentinel_linear_search(a, x):
    n = len(a)
    a.append(x) 
    i = 0
    while a[i] != x:
        i += 1
    a.pop()
    if i < n:
        return i
    else:
        return -1