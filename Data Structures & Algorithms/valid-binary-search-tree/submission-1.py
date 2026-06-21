# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            if not node: return True

            if not (left < node.val < right):
                return False

            left_sub_tree = valid(node.left, left, node.val)
            right_sub_tree = valid(node.right, node.val, right)

            return left_sub_tree and right_sub_tree

        return valid(root, float("-inf"), float("inf"))