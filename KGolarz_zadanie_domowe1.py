# 1
print("Zadanie 1")
#print()
x = range(-5,6)
for xx in x:
    print((5-abs(xx))*'x',abs(xx)*2*' ',(5-abs(xx))*'x',sep='')
    #print(xx)


'''
print('*        *')
print('**      **')
print('***    ***')
print('****  ****')
print('**********')
print('****  ****')
print('***    ***')
print('**      **')
print('*        *')
'''

# 2
print()
print("-------------------------------------------------------------------")
print("Zadanie 2")
print()
# 13TB = 13 * 1024GB = 13 * 1024 * 1024MB
# 194MB = 5s

print("13TB = 13 * 1024GB = 13 * 1024 * 1024MB")
print("194MB = 5s")
rozmiar = 13 * 1024 * 1024 # MB
znane = 194 / 5 # MB/s
czas = (1 / znane) * rozmiar # sekund
print("Pobranie ", rozmiar,"MB zajmie: ",round(czas/(60*60),2),'h',sep='')

# 3
print()
print("-------------------------------------------------------------------")
print("Zadanie 3")
print()

#zmienne
v_wlasne_srodki = 30000 #int(input("Jakie środki własne? "))
v_czestotlowosc = 4 #int(input("Jak często w roku? "))
czestotlowosc = range(1, v_czestotlowosc + 1)
oprocentowanie = [7.5, 8, 8.5]

#Pierwszy wpis
print("Wartosc poczatkowa", v_wlasne_srodki,"PLN")

#petla dla oprocentowania
for x in oprocentowanie:
    wartosc = v_wlasne_srodki
    print("   Oprocentowanie: ", x, "% - kwartalne",sep='')

    #petla dla czestotliwosci kapitalizacji
    for y in czestotlowosc:
        wartosc = wartosc * (1+(x * 0.01))
        ''' 
        print(y)
        print(wartosc)
        '''
        print("      Wartosc po ",y," kwartale = ",wartosc)
    print("         Zysk po roku: ",wartosc - v_wlasne_srodki, "PLN")

#
print()
print("Gdyby takie lokaty istnialy...")
# ciekawe skąd biorą się te końcówki...
