class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

a = Node(15)
b = Node(13)
a.next = b
print(a.data,b.data,sep=',')
print(a)
print(b)
print(a.next)