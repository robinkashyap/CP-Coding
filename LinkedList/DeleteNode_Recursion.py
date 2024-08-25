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
    if head is None:
        return 0
    return lenLL(head.next) + 1

def delLL(head,i):
    if i < 0 or i >= lenLL(head):
        print("Invalid i Value")
        return
    if head is None:
        return None
    if i == 0:
        head = head.next
        return head
    smallHead = delLL(head.next,i-1)
    head.next = smallHead
    return head

def printLL(head):
    while head is not None:
        print(str(head.data)+'->',end='')
        head = head.next
    print(None)
    return

head = inputLL()
pos = 2
# print(lenLL(head))
# printLL(head)
head = delLL(head,pos)
printLL(head)
