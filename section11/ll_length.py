"""
13.04.24
@author: дьяконенко денис
"""


class Node(object):
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


def length(node):
    length_node = 0
    ll = node
    while ll:
        length_node += 1
        ll = ll.next
    return length_node


def count(node, data):
    counter = 0
    ll = node
    while ll:
        if ll.data == data:
            counter += 1
        ll = ll.next
    return counter


if __name__ == "__main__":
    list1 = Node(1, Node(2, Node(3)))
    list2 = Node(
        1, Node(1, Node(1, Node(2, Node(2, Node(2, Node(2, Node(3, Node(3))))))))
    )
    print(length(list1))
    print(length(list2))
    print(count(list1, 2))
    print(count(list2, 2))
