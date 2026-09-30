"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # approach: use dfs
        # if the node is none, return none
        # make a hashmap traverse the entire graph
        # key = current node, value = the clone of that node
        # if the node is already in the hashmap, return its clone
        # otherwise make the clone, put it in the hashmap
        # for each neighbour in the current node, continue running the dfs recursively, append it to neighbour list

        hashmap = {}

        def dfs(node):
            if not node:
                return None

            clone = None

            if node in hashmap:
                return hashmap[node]
            else:
                clone = Node(node.val)
                hashmap[node] = clone

            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(node)

            



            