items = ['bóng đá', 'bóng rổ', 'game', 'trà đá', 'du lịch']
print(*items, sep=', ')
txt = input("ngoài ra mình còn thích: ")
items.append(txt)
print(*items, sep=', ')
i = 0
replacing_item = "Jojo" #replacing_item là thay đổi trong chuỗi
items[i] = replacing_item
n = 4
replacing_item = "One Piece" #replacing_item là thay đổi trong chuỗi
items[n] = replacing_item
print(items)