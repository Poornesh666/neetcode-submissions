# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root: return ""
        data = ""
        def dfs(root):
            nonlocal data
            if root:
                data += str(root.val) + ","
            else:
                data += "#,"
                return
            
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return data

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if len(data) == 0: return TreeNode("")

        store = data.split(",")[:-1]
        i = 0

        def dfs():
            nonlocal i
            
            if store[i] != "#": 
                root = TreeNode(int(store[i]))
                i += 1
                root.left = dfs()
                root.right = dfs()
            else:
                i += 1
                return None
                
            return root

        return dfs()

            