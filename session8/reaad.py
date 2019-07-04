items = ['bóng đá', 'bóng rổ', 'game', 'trà đá', 'du lịch']
print(*items, sep=', ')
txt = input("ngoài ra mình còn thích: ")
items.append(txt)
print(*items, sep=', ')
#index
print(items[0])
print(items[-1])
print(items[-2])