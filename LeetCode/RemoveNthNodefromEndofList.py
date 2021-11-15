# Given the head of a linked list remove the nth node from the end of the list and
# return the head.
class ListNode:
    def __init__(self, val = 0, next = None)
        self.val = val
        self.next = next
def removeNthfromend(head, n):
    dummy = ListNode(0, head)
    left = dummy
    right = head
    while n > 0 and right:
        right = right.next
        n -= 1
    while right:
        left = left.next
        right = right.next
    left.next = left.next.next
    return dummy.next
