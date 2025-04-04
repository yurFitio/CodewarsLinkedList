class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def push(head, data):
    new_node = Node(data)
    new_node.next, head = head, new_node
    return head

def build_one_two_three():
    head = None
    for nul in range(3, 0, -1):
        head = push(head, nul)
    return head
