import queue
class BinaryTree:
    def __init__(self,data) -> None:
        self.data = data
        self.right = None
        self.left = None

def levelWiseInput():
    q = queue.Queue()
    print("Enter root")
    rootdata = int(input())
    if rootdata == -1:
        return None
    root = BinaryTree(rootdata)
    q.put(root)
    while(not(q.empty())):
        curr_node = q.get()
        print("Enter the left child of ",curr_node.data)
        leftchilddata = int(input())
        if leftchilddata != -1:
            leftchild = BinaryTree(leftchilddata)
            curr_node.left = leftchild
            q.put(leftchild)
        print("Enter the right child of ",curr_node.data)
        rightchilddata = int(input())
        if rightchilddata != -1:
            rightchild = BinaryTree(rightchilddata)
            curr_node.right = rightchild
            q.put(rightchild)
    return root

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

root = levelWiseInput()
printTree(root)
