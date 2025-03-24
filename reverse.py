class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


def reverse(head):
    if not head or not head.next:
        return head

    new_head = reverse(head.next)
    head.next.next = head
    head.next = None

    return new_head
