items = ['bóng đá', 'bóng rổ', 'game', 'trà đá', 'du lịch']
print(*items, sep=', ')
n = input("ngoài ra mình còn thích: ")
items.append(n)
print(*items, sep=', ')
#index
print("Index 0")
print(items[0],items.upper())
print("Index -1 ")
print(items[-1],items.upper())
print("Index -2")
print(items[-2],items.upper())