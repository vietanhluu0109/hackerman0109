items = [23,3,1,9,2003]
print(items)
txt = int(input("enter a number: "))
# for i in range(len(items)):
if txt in items :
    print("found, position", items.index(txt))
else:
    print("not found in our list")
