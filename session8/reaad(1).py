items = ['bóng đá', 'bóng rổ', 'game', 'trà đá', 'du lịch']
print(*items, sep=', ')
n = input("ngoài ra mình còn thích: ")
items.append(n)
print(*items, sep=', ')
if n in items:
    print("Hello")
#index
print("Index 0")
print(items[0].upper())
print(items[-1].upper())
print(items[-2].upper())