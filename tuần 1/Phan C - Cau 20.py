danh_ba = []
def them_lien_he(ten, sdt):
    lien_he = {"ten": ten, "sdt": sdt}
    danh_ba.append(lien_he)
    print(f"da them lien he: {ten} - {sdt}")
def tim_sdt_theo_ten(ten_can_tim):
    for lh in danh_ba:
        if lh["ten"].lower() == ten_can_tim.lower():
            return lh["sdt"]
    return None
def tim_ten_theo_sdt(sdt_can_tim):
    for lh in danh_ba:
        if lh["sdt"] == sdt_can_tim:
            return lh["ten"]
    return None
def dem_lien_he_theo_dau_so(dau_so):
    dem = 0
    for lh in danh_ba:
        if lh["sdt"].startswith(dau_so):
            dem += 1
    return dem
def menu():
    while True:
        print("\n" + "="*30)
        print("Danh ba")
        print("1. them lien he moi")
        print("2. tim sdt theo ten")
        print("3. tim ten theo sdt")
        print("4. dem so lien he")
        print("5. xem danh ba")
        print("0. exit")
        print("="*30)
        
        chon = input("nhap chuc nang (0-5)): ")
        
        if chon == '1':
            ten = input("nhap ten: ")
            sdt = input("nhap sdt: ")
            them_lien_he(ten, sdt)
            
        elif chon == '2':
            ten = input("nhap ten can tim: ")
            ket_qua = tim_sdt_theo_ten(ten)
            if ket_qua:
                print(ket_qua)
            else:
                print(ten)
                
        elif chon == '3':
            sdt = input("nhap sdt: ")
            ket_qua = tim_ten_theo_sdt(sdt)
            if ket_qua:
                print(ket_qua)
            else:
                print(sdt)
        elif chon == '4':
            dau_so = input("nhap sdt can dem: ")
            so_luong = dem_lien_he_theo_dau_so(dau_so)
            print(f"{so_luong} lien he co so '{dau_so}'")
            
        elif chon == '5':
            print("\ndanh sach:")
            if len(danh_ba) == 0:
                print("danh ba trong")
            else:
                for i, lh in enumerate(danh_ba, 1):
                    print(f"{i}. {lh['ten']} - {lh['sdt']}")
                    
        elif chon == '0':
            print("bai")
            break
        else:
            print("thu lai")
if __name__ == "__main__":
    menu()