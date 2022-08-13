# Definition for singly-linked list.
class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = None


def reorderList(head):
    if not head:
        return []
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    prev, cur = None, slow.next
    while cur:
        nextt = cur.next
        cur.next = prev
        prev = cur
        cur = nextt
    slow.next = None

    head1, head2 = head, prev
    while head2:
        nextt = head1.next
        head1.next = head2
        head1 = head2
        head2 = nextt
