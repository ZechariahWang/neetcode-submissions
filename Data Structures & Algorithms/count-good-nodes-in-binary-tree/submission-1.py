# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # approach: use dfs
        # make a counter number of good ndoes
        # through each exploration, keep track of a max var (pass it as a param)
        # if there is any val that is < max val, then it isnt considered a good node
        # otherwise, if it is >= max val, number of good nodes += 1
        # at the end, return number of good nodes

        num_good = 0

        def dfs(node, max_val):
            
            nonlocal num_good
            if node is None:
                return None

            dfs(node.left, max(node.val, max_val))
            dfs(node.right, max(node.val, max_val))

            if node.val >= max_val:
                num_good += 1

            return 

            
        dfs(root, float('-inf'))
        return num_good

            
        