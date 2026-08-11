# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # approach: use bfs, iterate through each level
        # make a deque
        # make an order list
        # loop through the queue via while
        # make a levels list, this stores the value at each level
        # run a for loop through the length of the current queue
        # pop the left most value from the queue, and append to the level list
        # if there is a left node, append it to the queue
        # if there is a right node, append it to the queue
        # at the very end, append level list to order
        # after the bfs search is complete, run a for loop get the last element of every list in order appendt to res
        # return res

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

        res = []
        for i in range(len(order)):
            res.append(order[i][-1])

        return res


        