# Time Complexity - O(min(pos,n))
# Space Complexity - O(min(pos,n))

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def lenLL(head):
    if head is None:
        return 0
    return lenLL(head.next) + 1

def insert(head,pos,data):
    if pos < 0:
        return head
    if pos == 0:
        newNode = Node(data)
        newNode.next = head
        return newNode
    if head is None:
        return None
    smallHead = insert(head.next, pos-1, data)
    head.next = smallHead
    return head

def inputLL():
    inputList = [int(ele) for ele in input().split()]
    head, tail = None, None
    for data in inputList:
        if data == -1:
            break
        newnode = Node(data)
        if head is None:
            head, tail = newnode, newnode
        else:
            tail.next = newnode
            tail = newnode
    return head

def printLL(head):
    while head is not None:
        print(str(head.data)+'->',end='')
        head = head.next
    print("None")
    return

pos = 2
data = 2
head = inputLL()
printLL(head)
len = print("Length of Linked List is: ",lenLL(head))
head = insert(head,pos,data)
printLL(head)

