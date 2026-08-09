# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # approach: since its a binary search tree, left side will always be < right side
        # make a variable called node and assign it to root
        # loop through node using a while loop
        # at each node v, check the value of the left subnodes, then check the value of the right subnodes
        # i have two values, p and q (.val), compare v with those two p and q vals
        # if v > p and < q then it is inbetween the two nodes
        # if v < p and < q: its on the left side, target must be on the right, move right
        # if v > p and > q: its on the right side, target must be on the left, move left
        # if v == p oor == q, then its the same, it will be a descendant of itself according to LCA definition

        node = root

        while node:
            if node.val < p.val and node.val < q.val:
                node = node.right
            elif node.val > p.val and node.val > q.val:
                node = node.left
            else:
                return node

        