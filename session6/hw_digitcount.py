m = input("Enter a number")
n = int(m)

loop_count = 0
while n>0:
    n = (n//10)
    loop_count += 1 
print(loop_count)
    