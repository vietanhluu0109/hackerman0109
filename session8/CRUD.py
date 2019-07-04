txt = int(input("1 la C, 2 la R, 3 la U, 4 la D. ban chon cai nao: "))
while True:
    if txt == 1:
        print("Trong cac mon the thao sau: bong da, bong ro, bong tennis, ban muon them mon nao?: ")
        n = input("ngoài ra mình còn thích: ")
        print("Vay cac mon the thao se la: bong da, bong ro, bong tennis", n)
        break
    elif txt == 2:
        if txt == 2:
            items = ['cơm','phở','bún','cháo']
            print(items)
            txt = input("ngoài ra mình còn thích: ")
            items.append(txt)
            print(items)
            for item in items:
                print(item)
                break
        else: 
            print("Khong co phan tu nao ca!")
            break
    