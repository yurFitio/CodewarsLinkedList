class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    if not head or not head.next:
        raise ValueError
    
    l, r = head, head.next
    l_copy, r_copy = l, r
    
    while l_copy and l_copy.next and r_copy and r_copy.next:
        l_copy.next, r_copy.next = l_copy.next.next, r_copy.next.next
        l_copy, r_copy = l_copy.next, r_copy.next
    
    if l_copy:
        l_copy.next = None
    if r_copy:
        r_copy.next = None
    
    return Context(l, r)
