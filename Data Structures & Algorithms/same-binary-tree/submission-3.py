# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:   
        def dfs(p, q):
            if not p and not q: return True

            if not p or not q: return False

            same = (p.val == q.val)
            left_same = dfs(p.left, q.left)
            right_same = dfs(p.right, q.right)

            return same and left_same and right_same 

        return dfs(p,q)
        