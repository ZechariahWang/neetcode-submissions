# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseLinkedList(self, head):
        curr = head
        prev = None

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # approach: rever the linkedlist
        # remove the nth element
        # reverse it back
        # return the head of the reversed reversed linkedlist (aka just the normal original linkedlist)

        rev = self.reverseLinkedList(head)
        dummy = ListNode(0, rev)
        prev = dummy
        for i in range(n-1):
            prev = prev.next
        prev.next = prev.next.next

        return self.reverseLinkedList(dummy.next)


