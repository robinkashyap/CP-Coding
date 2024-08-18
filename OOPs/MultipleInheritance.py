class Mother:
    def __init__(self):
        self.motherName = "Manju"

class Father:
    def __init__(self):
        self.fatherName = "Ashok"

class Child(Father, Mother):
    def __init__(self, fatherName, motherName, name):
        super().__init__(fatherName)
        super().__init__(motherName)
        self.name = name
    
    def printChild(self):
        print("Father name:",self.fatherName)
        print("Child name: ", self.name)
    
first = Child("Rohan")
first.printChild()     # Here Print function of Father class is called because of the order of the inheritance as Father is inherited first in child class