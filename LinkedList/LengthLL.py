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


def takeInput():
    inputList = [int(ele) for ele in input().split()]
    head = None
    tail = None
    for currData in inputList:
        if currData == -1:
            break
        newNode = Node(currData)
        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
            
    return head

head = takeInput()
print(lenLL(head)) 