class Vehicle:
    def __init__(self,color,maxSpeed):
        self.color = color
        self.maxSpeed = maxSpeed
    
class Car(Vehicle):
    def __init__(self,color, maxSpeed, numGear, isConvertible):
        super().__init__(color,maxSpeed)
        self.numGear = numGear
        self.isConvertible = isConvertible
    
    def printCar(self):
        print("color: ", self.color)
        print("maxspeed: ", self.maxSpeed)
        print("numGear: ", self.numGear)
        print("isconvertible: ", self.isConvertible)

figo = Car("White", 220, 6, False)
figo.printCar()