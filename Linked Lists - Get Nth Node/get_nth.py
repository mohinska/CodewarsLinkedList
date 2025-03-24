from preloaded import Node

# class Node(object):
#     """Node class for reference"""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next


def get_nth(node, index):
    if node is None or index < 0:
        raise
    for _ in range(index):
        if node.next is None:
            raise
        node = node.next
    return node
