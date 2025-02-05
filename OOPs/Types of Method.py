class Student:
    school = "DAV"
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    
    @classmethod
    def getSchool(cls):
        print(Student.school)

    @staticmethod
    def info():
        print("This is Student class")

s1 = Student(90,80,85)
print(s1.avg())
s1.getSchool()
s1.info()