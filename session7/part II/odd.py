n = int(input("điền số bạn muốn mình đi đến là (nhớ là >0 nha <3): "))
while True:
    if n > 0:
        r3 = range(1, n, 2)
        print(*r3)
    else:
        print("tao bảo điền số lớn hơn 0 mà :Đ. Lại nào.")
    break