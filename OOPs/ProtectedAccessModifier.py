# In Python, protected member are like public members we can access them directly outside of the class as well.
# Protected member defined with single underscore '_'  --->  _maxSpeed
# So what's the use of Protected members - In Python, if you encounter a protected member, it's best to avoid modifying or accessing it directly whenever possible. 
# Respect the convention that it is intended for internal use within the class or its subclasses.


class Vehicle:
    def __init__(self,color,maxspeed):
        self.color = color
        self._maxSpeed = maxspeed
    
    def print(self):
        print("Color: ",self.color)
        print("Max Speed", self._maxSpeed)

class Car(Vehicle):
    def __init__(self,color,maxSpeed,numgear,isconvertible):
        super().__init__(color,maxSpeed)
        self.numGear = numgear
        self.isConvertible = isconvertible

    def print(self):
        # print("Color: ",self.color)
        # print("Max Speed", self._maxSpeed)                            
        print("Num Gear: ",self.numGear)
        print("Is Convertible: ",self.isConvertible)

# figo = Car("White", 220, 6, False)
# figo.print()
figo = Vehicle("White", 220)
figo.print()
figo._maxSpeed = 440
figo.print()

