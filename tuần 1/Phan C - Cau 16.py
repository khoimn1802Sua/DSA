def tim_phan_tu_gan_nhat(a, x):
    if len(a) == 0:
        return None, -1
    vt_min = 0
    khoang_cach_min = abs(a - x)
    for i in range(1, len(a)):
        khoang_cach_hien_tai = abs(a[i] - x)
        
        if khoang_cach_hien_tai < khoang_cach_min:
            khoang_cach_min = khoang_cach_hien_tai 
            vt_min = i
    return a[vt_min], vt_min