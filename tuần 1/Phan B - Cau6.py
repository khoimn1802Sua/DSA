def linearsearch(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1