def gtln(a):
    if len(a) == 0:
        return None
    vt_max = 0
    gt_max = a
    for i in range(1, len(a)):
        if a[i] > gt_max:
            gt_max = a[i]
            vt_max = i
    return vt_max
