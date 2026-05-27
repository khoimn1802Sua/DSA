def tim_so_chan_dau_tien(a):
    for i in range(len(a)):
        if a[i] % 2 == 0:
            return i
    return -1
a = [ ]
vi_tri = tim_so_chan_dau_tien(a)
if vi_tri != -1:
    print(f"so chan {a[vi_tri]} tai {[vi_tri]}")
else:
    print("khong co so chan")