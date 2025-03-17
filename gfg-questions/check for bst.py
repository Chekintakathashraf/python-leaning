"""Given the root of a binary tree. Check whether it is a BST or not.
Note: We are considering that BSTs can not contain duplicate Nodes.
A BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.

Examples:

Input: root = [2, 1, 3, N, N, N, 5]


Output: true 
Explanation: The left subtree of every node contains smaller keys and right subtree of every node contains greater keys. Hence, the tree is a BST.

Input: root = [2, N, 7, N, 6, N, 9] 



Output: false 
Explanation: Since the node to the right of node with key 7 has lesser key value, hence it is not a valid BST.

Input: root = [10, 5, 20, N, N, 9, 25]


Output: false
Explanation: The node with key 9 present in the right subtree has lesser key value than root node."""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_bst(root, min_value=float('-inf'), max_value=float('inf')):
    if not root:
        return True  # An empty tree is a BST
    
    if not (min_value < root.val < max_value):
        return False  # Current node violates BST rule
    
    return is_bst(root.left, min_value, root.val) and is_bst(root.right, root.val, max_value)

# Example Usage:

# Example 1: BST -> [2, 1, 3, None, None, None, 5]
root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(3)
root1.right.right = TreeNode(5)
print(is_bst(root1))  # Output: True

# Example 2: Not a BST -> [2, None, 7, None, 6, None, 9]
root2 = TreeNode(2)
root2.right = TreeNode(7)
root2.right.right = TreeNode(6)  # Wrong placement
root2.right.right.right = TreeNode(9)
print(is_bst(root2))  # Output: False

# Example 3: Not a BST -> [10, 5, 20, None, None, 9, 25]
root3 = TreeNode(10)
root3.left = TreeNode(5)
root3.right = TreeNode(20)
root3.right.left = TreeNode(9)  # Violates BST condition
root3.right.right = TreeNode(25)
print(is_bst(root3))  # Output: False
