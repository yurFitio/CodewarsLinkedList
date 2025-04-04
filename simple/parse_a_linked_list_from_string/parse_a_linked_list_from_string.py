class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


def linked_list_from_string(s):
    points = s.split(' -> ')[:-1][::-1]
    cur = None
    for point in points:
        cur = Node(int(point), cur)
    return cur
