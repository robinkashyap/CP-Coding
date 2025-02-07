class Default:
    def add(self,a=None,b=None,c=None):
        s = 0
        if(a!=None and b!=None and c!=None):
            s = a+b+c
        elif(a!=None and b!=None):
            s=a+b
        else:
            s = a
        return s
d = Default()
print(d.add(10,20,30))
print(d.add(10,20))
print(d.add(10))

class Args:
    def add(self,*args):
        s=sum(args)
        return s
a = Args()
print(a.add(10,20,30))
print(a.add(10,20))
print(a.add(10))

