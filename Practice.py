class Vehicle:
    def __init__(self,color,numGear):
        self.color = color
        self.numGear = numGear

class Car(Vehicle):
    def __init__(self,color,numGear,maxSpeed):
        Vehicle.__init__(self,color,numGear)
        self.maxSpeed = maxSpeed
    def printCar(self):
        print('Color: ',self.color)
        print('numGear: ',self.numGear)
        print('maxSpeed: ',self.maxSpeed)

bmw = Car("Black",6,220)
bmw.printCar()
