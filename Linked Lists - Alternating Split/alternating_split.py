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
        raise

    first_head = first_curr = head
    second_head = second_curr = head.next

    head = head.next.next
    toggle = True

    while head:
        if toggle:
            first_curr.next = head
            first_curr = first_curr.next
        else:
            second_curr.next = head
            second_curr = second_curr.next

        toggle = not toggle
        head = head.next

    first_curr.next = None
    second_curr.next = None
    return Context(first_head, second_head)
