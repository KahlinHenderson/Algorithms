# Given a linked list L0 --> L1 --> ... --> Ln-1 reorder the nodes to
# L0 --> Ln-1 --> L1 --> Ln-2 --> ...
def reorderList(head):
    if head == None or head.next == None:
        return
    l1 = head
    slow = head
    fast = head
    prev = None
    while fast != None and fast.next != None:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    prev.next = None
    l2 = reverse(slow)
    merge(l1, l2)
    def reverse(head):
        prev = None
        current_node = head
        while current_node != None:
            next_node = current_node.next
            current_node.next = prev
            prev = current_node
            current_node = next_node
        return prev
    def merge(l1, l2):
        while l1 != None:
            l1_next = l1.next
            l2_next = l2.next
            l1.next = l2
            if l1_next == None:
                break
            l2.next = l1_next
            l1 = l1_next
            l2 = l2_next
