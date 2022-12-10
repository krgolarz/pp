class Employee: # create class
    def set_salary(self,sal,nett): # create method
        self.salary = sal # i dont know
        self.netto = nett
e = Employee() # set Employee class for this variable
e.set_salary(123,130) # set value to the attribute
print(e.salary)
print(e.netto)
