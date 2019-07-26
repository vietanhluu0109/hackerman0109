items = ['cơm','phở','bún','cháo']
print(items)
# for i in range(len(items)):
# print(items)
txt = input("ngoài ra mình còn thích: ")
items.append(txt)
print(items)
for i, item in enumerate(items):
    print( i + 1, ",", item.upper())