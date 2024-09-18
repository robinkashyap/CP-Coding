# Build Tree from inorder and preorder
# Find the root - preorder[0]
# Splitting Inorder into Subtrees - Once we know the root node, we need to divide the inorder array into two parts:
#                                   1. The part to the left of the root in the inorder array corresponds to the left subtree.
#                                   2. The part to the right of the root in the inorder array corresponds to the right subtree.
# Recursion - After identifying the left and right subtrees from the inorder array:
#             Recursively build the left subtree by taking the corresponding left part of both the preorder and inorder arrays.
#             Recursively build the right subtree similarly by taking the corresponding right part of both arrays.
# Base Case - The recursion stops when there are no more elements to process, i.e., 
#             when either preorder or inorder arrays are empty, at which point the function returns None.

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def buildTree(inorder, preorder):
    if not preorder or not inorder:
        return None
    
    # Step 1: Get the root value from the first element of preorder
    root_Val = preorder[0]                             
    root = Node(root_Val)  # Create the root node                   
    
    # Step 2: Find the root index in the inorder traversal
    root_index = inorder.index(root_Val)                

    # Step 3: Slice the inorder list into left and right subtrees
    left_inorder = inorder[:root_index]                 # Elements before root in inorder
    right_inorder = inorder[root_index + 1:]            # Elements after root in inorder

    # Step 4: Slice the preorder list into left and right subtrees
    left_preorder = preorder[1:1 + len(left_inorder)]   # Elements for the left subtree in preorder
    right_preorder = preorder[1 + len(left_inorder):]   # Elements for the right subtree in preorder

    # Step 5: Recursively build left and right subtrees
    root.left = buildTree(left_inorder, left_preorder)
    root.right = buildTree(right_inorder, right_preorder)

    return root

def print_inorder(node):
    if node:
        print_inorder(node.left)
        print(node.data, end=" ")
        print_inorder(node.right)

# Example usage
inorder = [4, 2, 5, 1, 6, 3, 7]
preorder = [1, 2, 4, 5, 3, 6, 7]

root = buildTree(inorder, preorder)

print("Inorder traversal of the constructed tree:")
print_inorder(root)
