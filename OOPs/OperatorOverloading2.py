class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    
    def __add__(self,other):
        m1 = self.m1 + other.m1   # 118
        m2 = self.m2 + other.m2   # 134
        m3 = Student(m1,m2)       # created new student object with summed value (118,134)
        return m3                 # Returns the object

s1 = Student(58,69)
s2 = Student(60,65)
s3 = s1+s2                        # it calls s1.__add__(s2) 
print(s3.m1)