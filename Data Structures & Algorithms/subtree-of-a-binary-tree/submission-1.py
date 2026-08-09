# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # approach: use dfs
        # make a variable is_root = False
        # run dfs on that node and check if its equal to the sub root tree
        # this will be in the form of a helper function is_equal, which compare two subtrees and checks if they are equal (same logic as the same tree question)
        # for each iteration, pass it into the is_equal function to check if they are the same, once it returns true we know there is a valid subtree
        # once this is the case, set is_root to true
        # return is_root

        def is_equal(node1, node2):
            if not node1 and not node2:
                return True

            if not node1 or not node2:
                return False

            if node1.val != node2.val:
                return False

            left = is_equal(node1.left, node2.left)
            right = is_equal(node1.right, node2.right)

            return left and right

        def dfs(node):
            if not node:
                return False

            left = dfs(node.left)
            right = dfs(node.right)

            return is_equal(node, subRoot) or left or right

        return dfs(root)



        