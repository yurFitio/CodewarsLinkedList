def loop_size(node):
    slow, fast = node, node
    
    while slow and fast:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            start = slow
            slow = slow.next
            length = 1

            while slow != start:
                slow = slow.next
                length += 1 
            return length

    return None
