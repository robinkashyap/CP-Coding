# Time Complexity - O(n^2)
# Space Complexity - O(1)


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def printLL(head):
    while head is not None:
        print(str(head.data) +"->",end='')
        head = head.next
    print(None)
    return 

def takeInput():
    inputList = [int(ele) for ele in input().split()]
    head = None
    for currData in inputList:
        if currData == -1:
            break
        newNode = Node(currData)
        if head is None:
            head = newNode
        else:
            curr = head
            while curr.next is not None:
                curr = curr.next
            curr.next = newNode
    return head

head = takeInput()
printLL(head) 
