import random as rd

if 2 * 3 - 6 == 6:  # F
    print(1)
elif True and False:
    print(2)
else:
    print(3)  # return

if "Matematyka".find("test") == -1 or not 5 > 2:  # T || F
    print(1)  # return
elif 7 < 7:
    print(2)
else:
    print(3)

b = 5
if b == 1 or 2 or 4:  # "b == " missing for 2 and 4
    print(1)  # because 3 non equal to 4 but 3 is True (only 0 is False)
else:
    print(2)

if rd.randint(1, 3) > "czas".find("zegar"):  # T
    print(1)  # return
elif False:
    print(2)
else:
    print(3)
