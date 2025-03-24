def loop_size(node):
    slow = fast = node

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    length = 1
    slow = slow.next
    while slow != fast:
        length += 1
        slow = slow.next

    return length
