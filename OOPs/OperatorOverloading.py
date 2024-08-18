class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return "This point is at {" +str(self.x) + "," + str(self.y) +"}"
    
    def __add__(self,other):
        return Point(self.x + other.x, self.y + other.y)
    
p1 = Point(2,4)
p2 = Point(5,8)
p3 = Point(2,5)
p4 = p1+p2+p3
print(p4)