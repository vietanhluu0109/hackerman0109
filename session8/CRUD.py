while True:
    txt = int(input("1 la C, 2 la R, 3 la U, 4 la D. ban chon cai nao: "))
    if txt == 1:
        print("trong cac mon an sau: com, pho, bun, chao, ban co muon them gi khong? ")
        n = input("ngoai ra minh con thich: ")
        print("vay cac mon an se la: com, pho, bun, chao,", n)
        
    elif txt == 2:
        if txt == 2:
            items = ['com','pho','bun','chao']
            print(items)
            txt = input("ngoai ra minh con thich: ")
            items.append(txt)
            print(items)
            for item in items:
                print(item)
                break
        else: 
            print("khong co phan tu nao ca!")
            break
    elif txt == 3:
        items = ['cơm','phở','bún','cháo']
        txt = input("ban co muon thay doi gi khong: ")
        i = item
        replacing_item = txt #replacing_item là thay đổi trong chuỗi
        print[i] = replacing_item
        n = 4
    