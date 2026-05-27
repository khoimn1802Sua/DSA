def tim_tat_ca(a, x):
    danh_sach = []
    for i in range(len(a)):
        if a[i] == x:
            danh_sach.append(i)
    return danh_sach