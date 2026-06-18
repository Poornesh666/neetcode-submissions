# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(root1, root2):
            def dfs(root1, root2):
                if not root1 and not root2: return True
                if not root1 or not root2: return False

                same = root1.val == root2.val 
                left = dfs(root1.left, root2.left)
                right = dfs(root1.right, root2.right)   

                return same and left and right
            return dfs(root1, root2)

        def dfs(root, subroot):
            if not root and not subroot: return True
            if not root or not subroot: return False

            if isSameTree(root, subroot):
                return True
            else:
                return dfs(root.left, subroot) or dfs(root.right, subroot)
            
        
        return dfs(root, subRoot)
            

