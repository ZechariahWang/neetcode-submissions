# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # approach: run dfs on the tree
        # through each iteration, increase a count by 1
        # update max count once it reaches the end (aka, both left and right are null)

        max_count = 0
        
        def dfs(node, count):
            nonlocal max_count
            if not node:
                return

            count += 1
            max_count = max(max_count, count)
            dfs(node.left, count)
            dfs(node.right, count)

        dfs(root, 0)
        return max_count

        