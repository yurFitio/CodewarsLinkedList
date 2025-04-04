class Node:
    def __init__(self, next=None):
        self.next = next


def swap_pairs(head):
    if head is None or head.next is None:
        return head
    current = Node(head)
    new_head = head.next

    while current.next and current.next.next:
        a, b = current.next, current.next.next
        a.next = b.next
        b.next = a
        current.next = b
        
        current = current.next.next
    return new_head
