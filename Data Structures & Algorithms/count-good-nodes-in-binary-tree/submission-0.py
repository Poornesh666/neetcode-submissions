# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(root, max_so_far):
            if not root: 
                return

            nonlocal res

            if root.val >= max_so_far:
                res += 1
                max_so_far = max(max_so_far, root.val)
                dfs(root.left, max_so_far)
                dfs(root.right, max_so_far)
            else:
                dfs(root.left, max_so_far)
                dfs(root.right, max_so_far)

        dfs(root, root.val)
        return res