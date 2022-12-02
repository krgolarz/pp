import random

a = random.randint(1,4)

print("a=",a)

b = random.randint(1,10)
c = random.randint(1,10)

print("b=",b)
print("c=",c)

if a == 1:
    print("dodawanie:",b + c)
elif a == 2:
    print("odejmowanie",b - c)
elif a == 3:
    print("mnozenie",b * c)
else:
    print("dzielenie",b / c)
