
while True: 
    n = int(input("điền tháng bạn muốn biết bao nhiêu ngày trong tháng là: "))
    if n == 2:
        print("28 days")
    elif n in [1,3,5,7,8, 10,12]:
        print("31 days")
    elif n < 13:
        print("30 days")
    else:
        break