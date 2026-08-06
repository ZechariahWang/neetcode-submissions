# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # approach: use dfs 
        # at each node, check height of the left and right subtree, sutbract them and get the abs difference
        # if this abs difference > 1, we know its definitely not balanced, return false
        # otherwise, keep going an checking every node. if all pass, return true
        # time complexity: O(n), space complexity: O(1)

        balanced = True

        def dfs(node):
            nonlocal balanced
            if not node:
                return 0
            
            l = dfs(node.left)
            r = dfs(node.right)

            difference = abs(r - l)
            if difference > 1:
                balanced = False

            return 1 + max(l, r)

        dfs(root)
        return balanced