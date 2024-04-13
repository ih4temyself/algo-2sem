class Node(object):
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


def count(node, data=None) -> int:
    count = 0
    linked_list = node
    while linked_list:
        if data == None or linked_list.data == data:
            count += 1
        linked_list = linked_list.next
    return count


def length(node) -> int:
    return count(node)


if __name__ == "__main__":
    list1 = Node(1)
    list1.next = Node(2)
    list1.next.next = Node(3)

    list2 = Node(1)
    list2.next = Node(1)
    list2.next.next = Node(1)
    list2.next.next.next = Node(2)
    list2.next.next.next.next = Node(2)

    print(length(list1))
    print(length(list2))
    print(count(list1, 4))
    print(count(list2, 2))
