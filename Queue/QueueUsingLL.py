class Node:
    def __init__(self, data):
        self.data = data  # Store the data
        self.next = None  # Initialize the next pointer to None
        
class Queue:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count = 0
    
    def enqueue(self,data):
        newNode = Node(data)
        if self.__head is None:
            self.__head = newNode
        else:
            self.__tail.next = newNode
        self.__tail = newNode
        self.__count += 1
    
    def dequeue(self):
        if self.__head is None:
            print("Hey! queue is empty")
            return
        ele = self.__head.data
        self.__head = self.__head.next
        self.__count -= 1
        return ele

    def front(self):
        if self.__head is None:
            print("Hey! queue is empty")
            return
        ele = self.__head.data
        return ele
    
    def size(self):
        return self.__count
    
    def isEmpty(self):
        return self.size()==0