# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        

        # Algorithm 
        '''
        Check if root is None
        Go all the way down to a leaf node and compute 1 + its root.left value and then root.right

        example:
        2 - > parent.. -> root.left = 4
        4 -> root.left = null
        4 -> root.right = null

        if root is None: 
            return 0 

        1 + max(0,0) = 1 for 4 max depth

        '''