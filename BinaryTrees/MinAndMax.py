import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


#Representation of the Pair Class
class Pair :
    def __init__(self, minimum, maximum) :
        self.minimum = minimum
        self.maximum = maximum

def getMinAndMax(root) :
    #Your code goes here
    if root is None:
        return Pair(float('inf'),float('-inf'))

    left_pair = getMinAndMax(root.left)
    right_pair = getMinAndMax(root.right)

    minValue = min(root.data, left_pair.minimum, right_pair.minimum)
    maxValue = max(root.data, left_pair.maximum, right_pair.maximum)

    return Pair(minValue,maxValue)


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

root = treeInput()
result = getMinAndMax(root)
print(result.minimum,result.maximum)

