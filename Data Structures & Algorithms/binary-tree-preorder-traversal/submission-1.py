# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # Pre-order Sequence: Root → Left → Right
        # In-order Sequence: Left → Root → Right
        # Post-order Sequence: Left → Right → Root
        
        res = []
        
        def dfs(node):
            if not node:
                return None
            
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return res
        