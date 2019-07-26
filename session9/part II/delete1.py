R = 'red'
B = 'blue'
G = 'gray'

items = [R, B, G]
print(*items, sep =', ')

b = int(input("item to delete by number: "))
items.pop(b-1)
print("our new color list:")
for i, item in enumerate(items):
    print( i + 1, ",", item)

c = input("item to delete by word: ")
items.remove(c)
print("our new color list:")
for i, item in enumerate(items):
    print( i + 1, ",", item)