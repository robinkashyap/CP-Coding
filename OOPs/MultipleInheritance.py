# class Mother:
#     def __init__(self,name):
#         self.motherName = name

# class Father:
#     def __init__(self,name):                        
#         self.fatherName = name

# class Child(Father, Mother):                        # functions of Father class is called first because of the order of the inheritance as Father is inherited first in child class
#     def __init__(self,fatherName,motherName,name):
#         Father.__init__(self,fatherName)
#         Mother.__init__(self,motherName)
#         self.name = name
    
#     def printChild(self):
#         print("Father name:",self.fatherName)
#         print("Mother name:",self.motherName)
#         print("Child name: ", self.name)

class Mother:
    def __init__(self):
        self.motherName = "Manju"

class Father:
    def __init__(self):                        
        self.fatherName = "Ashok"

class Child(Father, Mother):   # functions of Father class is called first because of the order of the inheritance as Father is inherited first in child class
    def __init__(self,name):
        Father.__init__(self)
        Mother.__init__(self)
        self.name = name
    
    def printChild(self):
        print("Father name:",self.fatherName)
        print("Mother name:",self.motherName)
        print("Child name: ", self.name)


first = Child("Rohan")
first.printChild()     
