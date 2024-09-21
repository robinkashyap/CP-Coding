# Time Complexity - O(n)
import queue
class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

def rootToLeafPathsSumToK(root, k, path=''):
    if root is None:
        return
    path = path + str(root.data) +' '
    if root.left == None and root.right == None and root.data == k:
        print(path)
        return
    rootToLeafPathsSumToK(root.left,k-root.data,path)
    rootToLeafPathsSumToK(root.right,k-root.data,path)

def takeInput():
    levelOrder = [5,6,7,2,3,-1,1,-1,-1,-1,9,-1,-1,-1,-1]
    start = 0
    
    length = len(levelOrder)

    if length == 1:
        return None
    
    root = BinaryTreeNode(levelOrder[start])
    start += 1

    q = queue.Queue()
    q.put(root)

    while not q.empty():
        currentNode = q.get()

        leftChild = levelOrder[start]
        start += 1

        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)

        rightChild = levelOrder[start]
        start += 1

        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right = rightNode
            q.put(rightNode)

    return root


# Main function
root = takeInput()
k = 13
rootToLeafPathsSumToK(root, k)