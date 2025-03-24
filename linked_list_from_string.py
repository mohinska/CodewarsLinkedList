def linked_list_from_string(s):
    data = s.split(' -> ')
    data.pop()
    head = None
    while data:
        head = Node(int(data.pop()), head)
    return head
