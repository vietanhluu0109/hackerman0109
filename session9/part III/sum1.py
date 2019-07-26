items = [23,3,1,9,2003]
print(items)

a = sum(items)
print(a)

calc = 0 
for i in range(len(items)):
    calc = calc + items[i]

print(calc)