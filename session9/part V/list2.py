l1 = ['ST', 'BĐ', 'BTL', 'CG', 'ĐĐ', 'HBT']
l2 = [150300, 247100, 333300, 266800, 420900, 318000 ]
f = max(l2)
u = min(l2)
c = l2.index(f)
k = l2.index(u)
print("Quan co dong dan la:",l1[c], f)
print("Quan co thua dan la:",l1[k], u)