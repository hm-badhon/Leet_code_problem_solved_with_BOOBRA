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

# Example usage:
# Create the binary tree
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)

root2 = TreeNode(1)
root2.left = TreeNode(2)

# Create an instance of the solution class
sol = Solution()
# Call the diameterOfBinaryTree function and print the result
print(sol.diameterOfBinaryTree(root1))  # Output should be 3
print(sol.diameterOfBinaryTree(root2))  # Output should be 1
