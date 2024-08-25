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

# def findData(head,n):
#     a = lenLL(head)
#     if a == 0:
#         return -1
#     for i in range(a):
#         if head.data == n:
#             return i
#         if head.next == None:
#             return -1
#         else:
#             head = head.next

def findData(head,n):
    pos = 0
    while head is not None:
        if head.data == n:
            return pos
        pos += 1
        head = head.next
    return -1

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

head = inputLL()
n = 5
pos = findData(head,n)
print(pos)