R = 'red'
B = 'blue'
G = 'gray'

items = [R, B, G]
print("our color list: ")
print(*items, sep =', ')
txt = input("enter a new color: ")
print("our new color list: ")
print(*items, txt, sep =", ")