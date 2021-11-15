# Given the head of a linked list determine whether or not there's a cycle in the
# list. The list has a cycle if the reference of the last node is assigned to some
# other node.
def hasCycle(head):
    fastpointer = head
    slowpointer = head
    while fastpointer != None and fastpointer.next != None:
        fastpointer = fastpointer.next.next
        slowpointer = slowpointer.next
        if fastpointer == slowpointer:
            return True
    return False
