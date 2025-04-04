class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head) -> Node:
    if head is None or head.next is None:
        return head

    rev_list = reverse(head.next)
    head.next.next = head
    head.next = None

    return rev_list
