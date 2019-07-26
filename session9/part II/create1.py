R = 'red'
B = 'blue'
G = 'gray'

items = [R, B, G]
print(*items, sep =', ')

txt = int(input("enter position: "))
print("Color at position",txt, ":", items[txt - 1])