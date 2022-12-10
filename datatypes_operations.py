list1=["apple","banana","grapes"]
list1.append("strawberry")   # strawberry is added to the list
print(list1)
list1.pop()  # removes the last element from the list
print(list1)
list1.pop()
print(list1)

tuple1=(1,2,3,4)
# tuple1.pop()    tuple cannot be modified
# tuple1.append()  tuple cannot be modified
print(tuple1)

set1={"water","air","food"}
set1.add("shelter")   # adds an element to the set at random position
print(set1)
set1.add("clothes")
print(set1)
set1.pop()  # removes random element from the set
print(set1)

dict1={"fruit1":"apple","fruit2":"banana","veg1":"tomato"}
dict1.update({"veg2":"brinjal"})
print(dict1)
dict1.update({"veg3":"chilli"})  # updates the dictionary at the end
print(dict1)
dict1.pop("veg2")
print(dict1)