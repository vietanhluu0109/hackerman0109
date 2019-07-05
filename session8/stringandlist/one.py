items = ['bóng đá', 'bóng rổ', 'game', 'trà đá', 'du lịch']
print(*items, sep=' ')
txt = input("ngoài ra mình còn thích: ")
items.append(txt)
print("Name your things: ", *items, sep=', ')
print("your things: ")
for item in items:
    print(item)