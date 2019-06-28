while True: 
    txt = input("điền tên của mày vào đây nào: ")
    if txt.isdigit():
        print("tao bảo mày điền tên chứ có phải điền số đâu :D")
    else:
        print("tên nghe hay đấy")
        break

while True: 
    txt = input("nhập mật khẩu để xác minh mày là người nào :D ")
    print(txt)
    if txt.isalpha():
        print("ôk mmày là hooman")
        break
    else:
        print("mày muốn làm người hay làm chó")
