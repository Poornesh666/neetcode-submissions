# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def depth(self, root):
        if not root: return 0

        return 1 + max(self.depth(root.left), self.depth(root.right))

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True
        if not p or not q: return False

        p_left = self.depth(p.left)
        q_left = self.depth(q.left)
        p_right = self.depth(p.right)
        q_right = self.depth(q.right)

        if p_left != q_left or p_right != q_right:
            return False
        
        def dfs(p, q):
            if not p and not q: return True

            if not p or not q: return False

            same = (p.val == q.val)
            left_same = dfs(p.left, q.left)
            right_same = dfs(p.right, q.right)

            return same and left_same and right_same 

        return dfs(p,q)
        