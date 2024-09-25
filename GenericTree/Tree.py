class NodeTree:
    def __init__(self,data):
        self.data = data
        self.children = list()

def printTree(root):
    if root is None: # Edge case not base case
        return
    print(root.data)
    for child in root.children:
        printTree(child)

def detailedPrintTree(root):
    if root is None:
        return
    print(root.data, end = ": ")
    for child in root.children:
        print(child.data, end=' ')
    print()

    for child in root.children:
        detailedPrintTree(child)


n1 = NodeTree(5)
n2 = NodeTree(2)
n3 = NodeTree(9)
n4 = NodeTree(8)
n5 = NodeTree(7)
n6 = NodeTree(15)
n7 = NodeTree(1)

n1.children.append(n2)
n1.children.append(n3)
n1.children.append(n4)
n1.children.append(n5)
n3.children.append(n6)
n3.children.append(n7)

printTree(n1)
detailedPrintTree(n1)