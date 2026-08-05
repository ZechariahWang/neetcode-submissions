# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # approach use dfs
        # get the depth of the left subtree
        # do the same for the right subtree
        # keep a best variable
        # add the two counters together, update best if needed
        # return best

        best = 0

        def dfs(node):
            nonlocal best
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            current = left + right
            best = max(best, current)

            return 1 + max(left, right)

        dfs(root)
        return best
        