while True:
    txt = input("Đăng ký tên đăng nhập: ")
    if txt.isdigit():
        print("xin vui lòng nhập lại")
    else:
        print("một lựa chọn thông minh!")
        break

while True: 
    txt = input("xin vui lòng nhập mật khẩu")
    print(txt)
    if txt.isalpha():
        print("một lựa chọn sáng suốt!")
        break
    else:
        print("xin vui lòng nhập lại")
    
while True: 
    txt = input("xin vui lòng nhập email")
    print(txt)
    if txt.isalpha():
        print("bạn đã tạo thành công!")
        break
    else:
        print("xin vui lòng nhập lại")
    