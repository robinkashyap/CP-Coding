class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def prin(self):
        print(self.name, self.age)
    
    @staticmethod
    def hello():
        print("Hello")

s1 = Student("Robin",27)
s2 = Student("Shubham",28)
s1.prin()
s1.hello()