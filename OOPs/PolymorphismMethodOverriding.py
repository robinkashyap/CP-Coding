# Method Overriding - This involves a method in a subclass that has the same name and parameters 
# as a method in the parent class but provides a different implementation. 
# The method that gets called is determined at runtime based on the object's actual class.
# Means it decides on runtime if Class Car have a Print function then it will call that
# otherwise it will check in parent class Vehicle for print if it's not in vehicle class


class Vehicle:
    def __init__(self,color,maxspeed):
        self.color = color
        self.maxSpeed = maxspeed
    
    def print(self):
        print("Color: ",self.color)
        print("Max Speed", self.maxSpeed)

class Car(Vehicle):
    def __init__(self,color,maxSpeed,numgear,isconvertible):
        super().__init__(color,maxSpeed)
        self.numGear = numgear
        self.isConvertible = isconvertible

    def print(self):
        super().print()                              # This will call print function of class Vehicle
        print("Num Gear: ",self.numGear)
        print("Is Convertible: ",self.isConvertible)

figo = Car("White", 220, 6, False)
figo.print()



    
