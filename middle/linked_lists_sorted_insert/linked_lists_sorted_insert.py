class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def sorted_insert(head, data):
    new_node = Node(data)
    if not head or head.data > data:
        new_node.next = head
        return new_node
    head_copy = head
    while head_copy.next and head_copy.next.data < data:
        head_copy = head_copy.next
    new_node.next, head_copy.next = head_copy.next, new_node
    return head
