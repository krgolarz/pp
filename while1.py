"""
a = 1
b = 5

while a <= b:
    print("start",a,b)
    a += 1
    print("end",a,b)
print("Done")

while input("Type in 'pomidor' to play, 'haha' to stop: ") != "haha":
    print("pomidor")
print("end")


a = int(input("podaj pierwsza liczbe: "))
b = int(input("podaj druga liczbe: "))

if a >= b:
    while a >= b:
        print(a)
        a -= 1
else:
    while a <= b:
        print(a)
        a += 1


import time as tm
a = 5
b = 1
while a >= b:
    print(a)
    a -= 1
    tm.sleep(1)
print("end")
"""
a = 0
b = 0
ipt =    int(input("Podaj liczbe: "))

while ipt >= 0:
   b += ipt
   a += 1
   print("Liczba:", ipt, " Suma:", b, " cnt",a)
   ipt = int(input("Podaj liczbe: "))
print("b / a =", b / a)



