money = 46567.00
year_increase_percentage = 7.5
year_increase_percentage *= 0.01
#years = 3

print("Poczatkowy kapital",money)
print("Roczna stopa oprocentowania",year_increase_percentage*100,"%")

money *= (1+year_increase_percentage) #y1
money *= (1+year_increase_percentage) #y2
money *= (1+year_increase_percentage) #y3

print("Zysk po 3 latach wynosi",round(money,2))

