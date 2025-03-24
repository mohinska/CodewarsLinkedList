from preloaded import Node

'''
Node is defined in preloaded like this:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''


def push(head, data):
    new_head = Node(data)
    new_head.next = head
    return new_head


def build_one_two_three():
    head = Node(3)
    for i in range(2, 0, -1):
        print(i)
        head = push(head, i)
    return head
