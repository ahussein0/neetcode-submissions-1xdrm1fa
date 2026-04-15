# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #DFS
        if root is None:
            return root
        
        # swap the children
        root.left, root.right = root.right, root.left
        
        #recursive calls
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
    
        