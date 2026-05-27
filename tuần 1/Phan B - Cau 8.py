def dem_xuat_hien(a, x):
    dem = 0
    for i in range(len(a)):
        if a[i] == x:
            dem += 1
    return dem