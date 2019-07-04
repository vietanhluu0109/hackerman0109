items = ['bóng đá', 'bóng rổ', 'game', 'trà đá', 'du lịch']
print(*items, sep=' ') #seperate là dùng để chia khoảng cách bằng gì
txt = input("ngoài ra mình còn thích: ")
items.append(txt)
print(*items, sep=' ')