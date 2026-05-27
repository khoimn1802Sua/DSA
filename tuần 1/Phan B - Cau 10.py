def xuat_hien_cuoi_cung(a, x):
    for i in range(len(a)-1, -1, -1):
        if a[i] == x:
            return i
    return -1
def xuat_hien_cuoi_cung_2(a, x):
    vi_tri_cuoi = -1
    for i in range(len(a)):
        if a[i] == x:
            vi_tri_cuoi = i
    return vi_tri_cuoi