items = [100, 22, 19, 69, 84]
items.sort(reverse=True)
print("Diem cua nguoi choi la:")
for i, item in enumerate(items):
    print( i + 1, ",", item)

txt = int(input("enter your new highscore: "))
items.append(txt)
items.sort(reverse=True)
print("Diem cua nguoi choi la:")
for i, item in enumerate(items):
    print( i + 1, ",", item)