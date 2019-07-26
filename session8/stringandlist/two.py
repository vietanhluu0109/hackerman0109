import random
n = input("Enter a word: ")
print("Jumbled word: ")
for i in range(1):
    li = list(n)
    random.shuffle(li)
    print(''.join(li), and =)