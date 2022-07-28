# Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def reverseList(self, head):
        curr = None

        while head:
            next = head.next
            head.next = curr
            curr = head
            head = next

        return curr
