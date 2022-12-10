list1=[1,5,3,9,"apple"]
print(list1.index(9)) # returns the index value of the particular element
list2=[2,7,8,7]
print(list2.index(7)) # returns the index value of the element at its first occurence
print(list2.index(7,2)) # returns the index value of the element from the particular start position given


tuple1=(1,3,6,7,9,10)
print(tuple1.index(6))
print(tuple1.index(9))


set1={1,5,6,3,9}
# set1.index()  will throw an error as they are unordered


dict1={"key1":"value1","key2":"value2"}
# dict1.index("key1") will throw an error
print(dict1.get("key1"))

