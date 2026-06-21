# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        res = 0
        def dfs(root):
            if not root: return
            nonlocal n, res
            dfs(root.left)
            n += 1
            if n == k:
                res = root.val
            dfs(root.right)

        dfs(root)
        return res         
