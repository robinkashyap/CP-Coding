class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def inputLL():
    inputList = [int(ele) for ele in input().split()]
    head = None
    tail = None
    for curr in inputList:
        if curr == -1:
            break
        newNode = Node(curr)
        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
    return head

def lenLL(head):
    count = 0
    while head is not None:
        count += 1
        head = head.next
    return count

def delLL(head,i):
    if i < 0 or i >= lenLL(head):
        return head
    curr = head
    prev = None
    count = 0
    while count < i:
        prev = curr
        curr = curr.next
        count += 1
    curr = curr.next
    if prev is None:
        head = curr
    else:
        prev.next = curr
    return head




def printLL(head):
    while head is not None:
        print(str(head.data)+'->',end='')
        head = head.next
    print(None)
    return

pos = 5
head = inputLL()
print(lenLL(head))
printLL(head)
head = delLL(head,pos)
printLL(head)
