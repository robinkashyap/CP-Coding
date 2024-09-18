import queue
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


def treeInput():
    rootData = int(input())
    if rootData == -1:
        return None
    root = BinaryTreeNode(rootData)
    leftTree = treeInput()
    rightTree = treeInput()
    root.left = leftTree
    root.right = rightTree
    return root

def levelWisePrint(root):
    qp = queue.Queue()
    qp.put(root)
    while(not(qp.empty())):
        curr_node = qp.get()
        if curr_node is not None:
            print(curr_node.data,end=':')
        if curr_node.left:
            print(f'L:{curr_node.left.data}',end=',')
            qp.put(curr_node.left)
        if curr_node.right:
            print(f"R:{curr_node.right.data}")
            qp.put(curr_node.right)

root = treeInput()
nroot = insertDuplicateNode(root)
levelWisePrint(nroot)