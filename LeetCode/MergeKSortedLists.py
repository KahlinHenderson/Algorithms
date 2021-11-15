# Given k sorted linked lists merge them into one sorted linked list.
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
def PrintList(node):
    while node:
        print(node.data, end = "-->")
        node = node.next
    print("None")
def sortedmerge(a, b):
    if a is None:
        return b
    elif b is None:
        return a
    if a.data <= b.data:
        result = a
        result.next = sortedmerge(a.next, b)
    else:
        result = b
        result.next = sortedmerge(a, b.next)
    return result
def mergeklists(A, k):
    last = k-1
    while last:
        i,j = 0, last
        while i < j:
            A[i] = sortedmerge(A[i], A[j])
            i = i+1
            j = j-1
            if i >= j:
                last = j
    return A[0]
