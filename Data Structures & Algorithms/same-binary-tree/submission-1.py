# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: # empty trees
            return True

        if not p or not q: # one tree is null, other is not
            return False
        
        if p.val != q.val:
            return False

        return (self.isSameTree(p.left, q.left) and
        self.isSameTree(p.right, q.right))

        '''
        The three base cases (stopping conditions):

        not p and not q — both nodes are None. You've reached the end of both trees simultaneously → True (they match here)
        not p or not q — one is None but the other isn't. The trees have different shapes → False
        p.val != q.val — both nodes exist but hold different values → False
        
        '''

