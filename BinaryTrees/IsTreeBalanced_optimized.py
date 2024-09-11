# Time Complexity - O(n)

class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def printTree(root):
    if root == None:
        return
    print(root.data, end=" : ")
    if root.left != None:
        print("L",root.left.data, end = ", ")
    if root.right != None:
        print("R",root.right.data,end="")
    print()
    printTree(root.left)
    printTree(root.right)

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


def getHeightAndCheckBalanced(root):
    if root is None:
        return 0, True
    lh, isLeftBalanced = getHeightAndCheckBalanced(root.left)
    rh, isRightBalanced= getHeightAndCheckBalanced(root.right)
    h = 1 + max(lh,rh)
    if lh - rh > 1 or rh - lh > 1:
        return h, False
    
    if isLeftBalanced and isRightBalanced:
        return h, True
    else:
        return h, False
root = treeInput()
# printTree(root)
print(getHeightAndCheckBalanced(root))