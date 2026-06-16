# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def depth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        return 1 + max(self.depth(root.left), self.depth(root.right))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        left = self.depth(root.right)
        right = self.depth(root.left)

        isBalenced = True

        if not self.isBalanced(root.left) or not self.isBalanced(root.right):
            isBalenced = False

        if abs(left - right) > 1:
            isBalenced = False

        return isBalenced  