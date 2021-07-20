# An XOR linked list is a more memory efficient doubly linked list.
# Instead of each node holding next and prev fields,
# it holds a field named both, which is an XOR of the next node and the previous node.

class Node:
    def __init__(self, element):
        self.element = element
        self.both = 0

# Implement an XOR linked list;
# it has an add(element) which adds the element to the end,
# and a get(index) which returns the node at index.

# If using a language that has no pointers (such as Python),
# you can assume you have access to get_pointer and dereference_pointer functions
# that converts between nodes and memory addresses.


class XORLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.nodes = []

    def add(self, element):
        node = Node(element)
        if not self.tail:
            self.head = node
            self.tail = node
        else:
            self.tail.both = get_pointer(node) ^ self.tail.both
            node.both = get_pointer(self.tail)
            self.tail = node
        self.nodes.append(node)

    def get(self, index):
        node = self.head
        for i in range(index):
            next_addr = 0 ^ node.both

            if next_addr:
                node = dereference_pointer(next_addr)
        return node
