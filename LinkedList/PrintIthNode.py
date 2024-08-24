# Time Complexity - O(n)
# Space Complexity - O(1)


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def printIthNode(head,i):
    count = 0
    while head is not None:
        if count == i:
            print(head.data)
            break
        count += 1
        head = head.next
    
def takeInput():
    inputList = [int(ele) for ele in input().split()]
    head = None
    tail = None
    for i in inputList:
        if i == -1:
            break
        newNode = Node(i)
        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
    return head
head = takeInput()
printIthNode(head,2) 