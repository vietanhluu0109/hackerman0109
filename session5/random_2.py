from random import randint

a = randint(1, 100)

print(a)
if a < 30:
    print("rainy")
elif 30 < a < 60:
    print("cloudy")
else:
    print("sunny")