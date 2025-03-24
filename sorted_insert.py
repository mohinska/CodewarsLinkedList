class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def sorted_insert(head, data):
    if not head or head.data > data:
        return Node(data, head)

    curr = head
    while True:
        if curr.data < data and curr.next is None or curr.next.data > data:
            curr.next = Node(data, curr.next)
            return head
        curr = curr.next
