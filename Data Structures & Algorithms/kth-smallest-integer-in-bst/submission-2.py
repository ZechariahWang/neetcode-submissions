# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # approach: use dfs in order traversal
        # in order is already sorted since its a BST go left -> root -> right
        # make a nonlocal counter started at 1
        # through each iteration, increase counter by 1
        # once counter == k, return that current node value
        # time complexity: O(h+k), space complexity: O(h)

        counter = 0
        value = None

        def dfs(node):
            nonlocal counter
            nonlocal value

            if node is None:
                return

            dfs(node.left)

            counter += 1
            if counter == k:
                value = node.val
                return

            dfs(node.right)

        dfs(root)
        return value

        
