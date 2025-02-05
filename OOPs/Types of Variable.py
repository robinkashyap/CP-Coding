class Car:
    wheels = 4
    def __init__(self):
        self.com = "BMW"
        self.mil = 6
    
c1 = Car()
c2 = Car()
c2.mil = 3
print(c1.com,c1.mil,Car.wheels)
print(c2.com,c2.mil,Car.wheels)
Car.wheels = 5
print(c1.com,c1.mil,c1.wheels)
print(c2.com,c2.mil,c2.wheels)
