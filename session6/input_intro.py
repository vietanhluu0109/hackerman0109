while True:
    txt = input("điền năm sinh của mày vào đây đi nào ")
    print(txt)
    if txt.isdigit():
        print("ôk tuổi của mày sẽ xuất hiện ngay đây thôi")
        break
    else:
        print("tao bảo mày điền năm sinh cơ mà")
print(2019- int(txt))
