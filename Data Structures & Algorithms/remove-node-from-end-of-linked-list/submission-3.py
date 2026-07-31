# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # approach: use two pointers
        # start l at dummy node behind head
        # start r at the head of the linkedlist
        # iterate until n < 0, decrementing n each time move each pointer up
        # once r is null (aka goes beyond the linkedlist), l shoul dbe pointeed at the node right behind the n node
        # assign that node next to be node next next
        # return dummy.next

        dummy = ListNode(0, head)
        l = dummy
        r = head
        
        while n > 0:
            r = r.next
            n -= 1

        while r:
            l = l.next
            r = r.next

        l.next = l.next.next
        return dummy.next


