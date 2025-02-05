class Person:
    def __init__(self):
        self.name = "Robin Kashyap"
        self.age = 26
    
    def update(self):
        self.age = 27

    def compare(self,other):
        if (self.age == other.age):
            return True
        else:
            return False

c1 = Person()
c2 = Person()
print(c1.compare(c2))
c2.update()
print(c1.name,c1.age,c2.name,c2.age, sep='\n')