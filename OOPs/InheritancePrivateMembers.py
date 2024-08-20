class Vehicle:
    def __init__(self,color,maxspeed):
        self.color = color
        self.__maxSpeed = maxspeed  # Private member - access only within the class
    
    def getMaxSpeed(self):          # we need to create a function (getter) to access the private member
        return self.__maxSpeed      # outside the class
    
    def setMaxSpeed(self,maxSpeed): # Setter function used to modified private member value
        self.__maxSpeed = maxSpeed


class Car(Vehicle):
    def __init__(self,color,maxSpeed,numGear, isConvertible):
        super().__init__(color,maxSpeed)
        self.numGear = numGear
        self.isConvertible = isConvertible
    def printCar(self):
        print("color: ", self.color)
        print("maxspeed: ", self.getMaxSpeed())
        print("numGear: ", self.numGear)
        print("isconvertible: ", self.isConvertible)
        print()

figo = Car("White", 220, 6, False)
figo.printCar()
figo.setMaxSpeed(440)
print("After modifying the private member value\n")
figo.printCar()