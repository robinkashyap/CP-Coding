import queue
class BinaryTree:
    def __init__(self,data) -> None:
        self.data = data
        self.right = None
        self.left = None

def nodeToRoot(root,s):
    if root is None:
        return None
    if root.data == s:
        l = list()
        l.append(root.data)
        return l
    
    leftOutput = nodeToRoot(root.left,s)
    if leftOutput != None:
        leftOutput.append(root.data)
        return leftOutput
    
    rightOutput = nodeToRoot(root.right,s)
    if rightOutput != None:
        rightOutput.append(root.data)
        return rightOutput
    else:
        return None 
    
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

root = levelWiseInput()
print(nodeToRoot(root,5))
