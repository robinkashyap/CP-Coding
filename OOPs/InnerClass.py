class Student:
    def __init__(self):
        self.name = "Robin"
        self.age = 27
        #self.lap = self.Laptop(brand)

    def show(self):
        print(self.name,self.age, sep=",")
        #self.lap.show()

    class Laptop:
        def __init__(self,brand):
            self.brand = brand
            self.cpu = "i5"

        def show(self):
            print(self.brand,self.cpu, sep=",")

s1 = Student()
# s1 = Student("HP")
lap1 = Student.Laptop("HP")
s1.show()
lap1.show()