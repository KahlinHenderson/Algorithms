# Given the head of a linked list reverse the list.
class ListNode:
    def __init__(self, val, next = None)
        self.val = val
        self.next = next
def ReverseRecursively(node):
    if node == None or node.next == None:
        return node
    head = ReverseRecursively(node.next)
    node.next.next = node
    node.next = None
    return head
def printList(head):
    while head != None:
        print(head.val, end = '-->')
        head = head.next

