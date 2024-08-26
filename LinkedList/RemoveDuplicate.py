class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def removeDuplicate(head):
    if head is None:
        return head  
    curr = head  
    while curr.next is not None:
        if curr.data == curr.next.data:
            # Skip the duplicate node
            curr.next = curr.next.next
        else:
            # Move to the next distinct node
            curr = curr.next 
    return head
   

def inputLL():
    inputLL = [int(ele) for ele in input().split()]
    head = None
    tail = None
    for data in inputLL:
        if data == -1:
            break
        newNode = Node(data)
        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
    return head

def printLL(head):
    while head is not None:
        print(str(head.data)+'->',end='')
        head = head.next
    print(None)
    return

head = inputLL()
head = removeDuplicate(head)
printLL(head)