a = input("Podaj nazwe miesiaca: ")

if a == "Styczen" or a == "Marzec" or a == "Maj" or a == "Lipiec" or a == "Sierpien" or a == "Pazdziernik" or a == "Grudzien":
    print(31)
elif a == "Luty":
    print(28)
else:
    print(30)