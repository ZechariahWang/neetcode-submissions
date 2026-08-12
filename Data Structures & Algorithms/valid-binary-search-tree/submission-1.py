# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # approach: use in order traversal, dfs
        # in order left -> root -> right
        # set the initial global nonlocal prev val var to be -inf, and iterate through the entire tree
        # if the values > the prev, its still valid so keep going
        # if it ever becomes less, then since its a bst, itll be invalid since we're going left -> right, return False
        # otherwise at the end, return True if none of the false conditions are met
        # Time complexity: O(n), space complexity: O(h)

        prev = float('-inf')
        is_valid = True

        def dfs(node):
            nonlocal prev
            nonlocal is_valid

            if node is None:
                return None

            dfs(node.left)

            if node.val <= prev:
                is_valid = False
            else:
                prev = node.val
                
            dfs(node.right)

        dfs(root)
        return is_valid




            