def tim_ten(ds, ten):
    ten_chuan = ten.strip().lower()
    for i in range(len(ds)):
        if ds[i].strip().lower() == ten_chuan:
            return i
    return -1
