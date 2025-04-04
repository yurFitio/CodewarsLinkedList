class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
def get_nth(node, index):
    if index < 0 or not isinstance(node, Node):
        raise ValueError
    for _ in range(index):
        node = node.next
        if not isinstance(node, Node):
            raise ValueError
    return node
  