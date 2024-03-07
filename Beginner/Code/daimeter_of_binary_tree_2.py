class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root):
        # Variable to store the maximum diameter
        self.max_diameter = 0
        
        # Helper function to calculate the height of each node
        def height(node):
            if not node:
                return 0
            
            # Calculate height of left and right subtrees
            left_height = height(node.left)
            right_height = height(node.right)
            
            # Update maximum diameter
            self.max_diameter = max(self.max_diameter, left_height + right_height)
            
            # Return height of the subtree rooted at 'node'
            return 1 + max(left_height, right_height)
        
        # Call the helper function to calculate height, which indirectly updates the maximum diameter
        height(root)
        
        return self.max_diameter

def list_to_tree(nums):
    print('nums :',nums)
    if not nums:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in nums]
    children = nodes[::-1]
    root = children.pop()
    for node in nodes:
        if node:
            if children: node.left = children.pop()
            if children: node.right = children.pop()
    return root

# Example usage:
# Input tree in list format
input_tree = [1, 2, 3, 4, 5]

# Convert list to binary tree
root = list_to_tree(input_tree)

# Create an instance of the solution class
sol = Solution()

# Call the diameterOfBinaryTree function and print the result
print(sol.diameterOfBinaryTree(root))  # Output should be 3
