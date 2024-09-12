class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

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

def heightAndDiameter(root):
    if root is None:
        return 0, 0  # (height, diameter)

    left_height, left_diameter = heightAndDiameter(root.left)
    right_height, right_diameter = heightAndDiameter(root.right)

    # Current height is the maximum height of its subtrees plus one
    current_height = 1 + max(left_height, right_height)

    # Diameter passing through the current node (left_height + right_height)
    diameter_through_root = left_height + right_height

    # The maximum diameter encountered so far
    current_diameter = max(diameter_through_root, left_diameter, right_diameter)

    return current_height, current_diameter

root = treeInput()
print(heightAndDiameter(root))