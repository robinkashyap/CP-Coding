from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insertDuplicateNode(root):
    # Your code goes here
    if root is None:
        return
    insertDuplicateNode(root.left)
    insertDuplicateNode(root.right)
    newNode = BinaryTreeNode(root.data)
    temp = root.left
    root.left = newNode
    newNode.left = temp
    return root

def takeinput():
    q = queue.Queue()
    rootdata = int(input())
    if rootdata == -1:
        return
    root = BinaryTreeNode(rootdata)
    q.put(root)
    while(not(q.empty())):
        curr_node = q.get()
        leftChilddata = int(input())
        if leftChilddata != -1:
            leftChild = BinaryTreeNode(leftChilddata)
            curr_node.left = leftChild
            q.put(leftChild)
        rightChilddata = int(input())
        if rightChilddata != -1:
            rightChild = BinaryTreeNode(rightChilddata)
            curr_node.right = rightChild
            q.put(rightChild)
    return root

def printLevel(root):
    q=queue.Queue()
    if root is None:
        return
    q.put(root)
    q.put(None)
    while(not(q.empty())):
        curr_node = q.get()
        if curr_node is None:
            print()
            if not(q.empty()):
                q.put(None)
        else:
            print(curr_node.data, end=' ')
        
            if curr_node.left:
                q.put(curr_node.left)
            if curr_node.right:
                q.put(curr_node.right)

root = takeinput()
root = insertDuplicateNode(root)
printLevel(root)

    