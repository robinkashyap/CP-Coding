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

def inputLL():
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

def reverseLL(head):
    if head is None:
        return head
    previous = None
    current = head

    while current is not None:
        new_node = current.next
        current.next = previous
        previous = current
        current = new_node
    
    return previous

def printLL(head):
    while head is not None:
        print(str(head.data)+'->',end='')
        head = head.next
    print(None)
    return

head = inputLL()
head = reverseLL(head)
printLL(head)