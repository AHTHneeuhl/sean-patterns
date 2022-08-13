# Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def removeElements(self, head, val):
        curr = ListNode(-1)
        curr.next = head
        start = curr
        while start.next:
            if start.next.val == val:
                start.next = start.next.next
            else:
                start = start.next
        return curr.next
