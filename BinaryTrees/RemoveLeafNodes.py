class BinaryTree:
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None

def treeInput():
    rootdata = int(input())
    if rootdata == -1:
        return
    root = BinaryTree(rootdata)
    leftNode = treeInput()
    rightNode = treeInput()
    root.left = leftNode
    root.right = rightNode
    return root

def printTree(root):
    if root is None:
        return
    print(root.data, end = ":")
    if root.left != None:
        print("L",root.left.data, end = ", ")
    if root.right != None:
        print("R",root.right.data, end = "")
    print()
    printTree(root.left)
    printTree(root.right)

def removeLeaf(root):
    if root is None:
        return
    if root.left == None and root.right == None:
        return None
    root.left = removeLeaf(root.left)
    root.right = removeLeaf(root.right)
    return root
root = treeInput()
printTree(root)
print("After removing Leaf Node")
root = removeLeaf(root)
printTree(root)