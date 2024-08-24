# Time Complexity - O(n)
# Space Complexity - O(1)


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def lenLL(head):
    count = 0
    while head is not None:
        count += 1
        head = head.next
    return count

def insertAtI(head,i,data):
    if i < 0 or i > lenLL(head):
        return head
    curr = head
    prev = None
    count = 0
    while count<i:
        prev = curr
        curr = curr.next
        count += 1

    newNode = Node(data)
    if prev is None:
        head = newNode
    else:    
        prev.next = newNode
    newNode.next = curr
 
    return head

def printLL(head):
    while head is not None:
        print(str(head.data) +"->",end='')
        head = head.next
    print(None)
    return 


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
printLL(head)
head=insertAtI(head,2,3)
printLL(head)
head=insertAtI(head,0,0)
printLL(head)
head=insertAtI(head,7,7)
printLL(head)