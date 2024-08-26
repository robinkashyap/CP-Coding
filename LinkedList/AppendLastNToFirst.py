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

def appendLastNToFirst(head,n):
    if head is None or n<=0:
        return head
    len = lenLL(head)
    curr = head
    prev = None
    pos = len - n
    for i in range(pos):
        prev = curr
        curr = curr.next
    new_head = curr
    while curr.next is not None:
        curr= curr.next
    curr.next = head
    if prev is not None:
        prev.next = None

    return new_head

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
n = 3
head = appendLastNToFirst(head,n)
printLL(head)