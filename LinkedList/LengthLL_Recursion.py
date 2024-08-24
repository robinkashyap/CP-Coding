class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def lenLL(head):
    if head == None:
        return 0
    return lenLL(head.next) + 1

def takeInput():
    inputList = [int(ele) for ele in input().split()]
    head = None
    tail = None
    for currData in inputList:
        if currData == -1:
            break
        newNode = Node(currData)
        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
            
    return head

head = takeInput()
print(lenLL(head)) 