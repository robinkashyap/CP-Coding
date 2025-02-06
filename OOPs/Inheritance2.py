class Veh:
    def __init__(self,color,maxSpeed):
        self.color = color
        self.maxSpeed = maxSpeed

class Car(Veh):
    def __init__(self,gear,isConvertible,color,maxSpeed):
        Veh.__init__(self,color,maxSpeed)
        self.gear = gear
        self.isConvertible = isConvertible
    def show(self):
        print(self.color,self.gear,self.maxSpeed,self.isConvertible,sep=",")
    
c1 = Car(6,True,"Red",300)
c1.show()