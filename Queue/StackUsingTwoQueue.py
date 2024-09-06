import queue
class StackUsingTwoQueue:
    def __init__(self):
        self.__q1 = queue.Queue()
        self.__q2 = queue.Queue()

    def push(self,data):
        self.__q1.put(data)
    
    def pop(self):
        if (self.__q1.qsize()==0):
            return -1
        while(self.__q1.qsize()>1):
            self.__q2.put(self.__q1.get())
        ele = self.__q1.get()
        while(self.__q2.qsize()>0):
            self.__q1.put(self.__q2.get())
        return ele
    
    def top(self):
        if (self.__q1.qsize()==0):
            return -1
        while(self.__q1.qsize()>1):
            self.__q2.put(self.__q1.get())
        top_ele = self.__q1.get()
        self.__q2.put(top_ele)
        while(self.__q2.qsize()>0):
            self.__q1.put(self.__q2.get())
        return top_ele
    
        # Check if the stack is empty
    def is_empty(self):
        return self.__q1.qsize() == 0

    # Get the size of the stack
    def size(self):
        return self.__q1.qsize()

# Example usage:
stack = StackUsingTwoQueue()
stack.push(10)
stack.push(20)
stack.push(30)

print(stack.pop())  # Output: 30
print(stack.top())  # Output: 20
print(stack.size()) # Output: 2