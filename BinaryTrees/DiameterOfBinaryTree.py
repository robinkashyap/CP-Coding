# Time Complexity - O(n^2)

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

def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))

def diameter(root):
    if root is None:
        return 0
    # Diameter passes through the root
    root_dia = height(root.left) + height(root.right)
    # Diameter is in left subtree
    left_dia = diameter(root.left)
    # Diameter is in right subtree
    right_dia = diameter(root.right)

    return max(root_dia, left_dia, right_dia)

root = treeInput()
# printTree(root)
print(diameter(root))