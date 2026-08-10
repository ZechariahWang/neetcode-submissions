# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # approach: run bfs:
        # if the root is None, just return empty list
        # convert the root to a deque
        # make an order list 
        # loop through the entire queue
        # at the beginning of each iteration make a level list
        # run a for loop throughout the length of the queue
        # as we do this, pop the left most node from queue and append it to level list
        # if there is a left node, append left node to queue
        # if there is a right node, append right node to queue
        # append level list to order list

        if root is None:
            return []

        queue = deque([root])
        order = []

        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            order.append(level)

        return order
        