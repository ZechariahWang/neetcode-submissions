# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # approach: make a new res linkedist (node)
        # loop while both lists still have something to compare
        # check which value is smaller, attach smaller node to node.next
        # dummy = a throwaway node; tail = bookmark, starts on dummy, always sits on the last node added
        # keep the pointer at the current node in the other list tho
        # continue this loop until all nodes have been added to res from one list
        # then just add the remianing nodes from the leftover list
        # Return dummy.next, which is the head of the merged list.

        dummy = res = ListNode(0)
        l1=0
        l2=0

        while list1 and list2:
            if list1.val < list2.val:
                res.next = list1
                list1 = list1.next
            else:
                res.next = list2
                list2 = list2.next
            res = res.next

        res.next = list1 or list2
        return dummy.next

