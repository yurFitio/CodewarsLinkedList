class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


def stringify(node):
    nodes = []
    while hasattr(node, 'data'):
        nodes.append(node.data)
        node = node.next
    return ' -> '.join(str(el) for el in nodes + [None])
