list1=["hello",1,4,8,"good"]
print(list1)
list1[0]="morning"  # assigning values ("hello" is replaced with "morning")
print(list1)
print(list1[4])
print(list1[-1]) # list also allow negative indexing
print(list1[1:4]) # slicing
list2=["apple","mango","banana"]
print(list1+list2) # list concatenation

tuple1=("good",1,2,3,"morning")
print(tuple1)
print(tuple1[0])  # accessing values using indexing
#tuple1[1]="change"  # a value cannot be changed as they are immutable
tuple2=("orange","grapes")
print(tuple1+tuple2)  # tuples can be concatenated
tuple3=(1,2,3)
print(type(tuple3))

set1={1,2,3,4,5}
print(set1)
# set1[0]   sets are unordered, so it doesnot support indexing
set2={3,7,1,6,1} # sets doesnot allow duplicate values
print(set2)

dict1={"key1":1,"key2":"value2",3:"value3"}
print(dict1.keys())  # all the keys are printed
dict1.values() # all the values are printed
dict1["key1"]="replace_one"  # value assigned to key1 is replaced
print(dict1)
print(dict1["key2"])