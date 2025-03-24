def stringify(node):
    repr = ''
    while node:
        repr += f"{node.data} -> "
        node = node.next
    repr += "None"
    return repr
