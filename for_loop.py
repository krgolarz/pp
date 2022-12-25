# ceate a list
'''
lista = ['one','two','three','four']
a = 0
for x in lista:

    print(x)
    lista.append(x)
    a += 1
    if a==10:
        break

for x in range(1, 11):
    for y in range(1, 11):
        print('%d * %d = %d' % (x, y, x*y))

a = 135
b = 3
print('%d * %d = %s' % (a,b, a * b))



for x in range(0, 10):
    for y in range(0, 10):
        for z in range(0, 10):
            print('%d + %d  + %d  = %d' % (x*100, y*10, z, 100*x+10*y+z))
'''
for x in range(0,11,2):
    print(x)