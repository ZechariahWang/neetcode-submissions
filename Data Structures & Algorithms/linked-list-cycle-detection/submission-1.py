# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # approach: use a hashset, loop through the entire LL and store all the nodes
        # For each iteration, check if the node.next is already inside the hashset, if it is then that means theres a loop

        hashset = set()

        curr = head
        while curr:
            if curr in hashset:
                return True
            hashset.add(curr)
            curr = curr.next
                             
        return False
        