"""
The other difference in python inheritance is
the fact you can have multiple parent classes.
Other languages usually only can have 1 class.
"""

# Base class1
class Mother:
    def __init__(self, motherName) -> None:
        self.motherName = motherName 
    
    def getName(self):
        print(self.motherName)

# Base class2
class Father:
    def __init__(self, fatherName) -> None:
        self.fatherName = fatherName 
    
    def getName(self):
        print(self.fatherName)

 
# Derived class
class Child(Mother, Father):        

    def parents(self):
        print("Father :", self.fatherName)
        print("Mother :", self.motherame)
"""
Running the code below shows that jose can have 2 variables,
inherited from separate classes, showing pythons multi class
inheritance
""" 

# Driver's code
jose = Child("Jose")
jose.fatherName = "Peter"
jose.motherName = "Maria"
jose.parents()