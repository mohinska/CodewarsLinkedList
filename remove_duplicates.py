class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def remove_duplicates(head):
    if not head:
        return

    pointer = head
    while pointer.next:
        if pointer.data == pointer.next.data:
            pointer.next = pointer.next.next
        else:
            pointer = pointer.next
    return head
