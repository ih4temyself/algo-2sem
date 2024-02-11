class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head_node = None
        self.tail_node = None

    def insert_to_start(self, data):
        new_node = Node(data)

        if self.head_node is None:
            self.head_node = new_node
            self.tail_node = new_node        

        else:
            new_node.next = self.head_node
            self.head_node.prev = new_node
            self.head_node = new_node

    def insert_to_end(self, data):
        new_node = Node(data)

        if self.tail_node is None:
            self.head_node = self.tail_node = new_node

        else:
            self.tail_node.next = new_node
            new_node.prev = self.tail_node
            self.tail_node = new_node

        
    def remove_head(self):
        if self.head_node is None:
            return
        
        if self.head_node == self.tail_node:
            self.head_node = self.tail_node = None
        else:
            next_node = self.head_node.next
            self.head_node = next_node
            if next_node:
                next_node.prev = None

    def remove_tail(self):
        if self.tail_node is None:
            return
        
        if self.head_node == self.tail_node:
            self.head_node = self.tail_node = None
        else:
            prev_node = self.tail_node.prev
            self.tail_node = prev_node
            if prev_node:
                prev_node.next = None


    def size(self) -> int:
        counter = 0 
        marker = self.head_node
        while marker:
            counter += 1
            marker = marker.next
        return counter

    def show(self):
        current = self.head_node
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


if __name__ == '__main__':
    doubly_linked_list = DoublyLinkedList()

    doubly_linked_list.insert_to_end('a')
    doubly_linked_list.insert_to_end('b')
    doubly_linked_list.insert_to_start('c')
    doubly_linked_list.insert_to_end('d')

    print("Node Data")
    doubly_linked_list.show()

    print("Remove First Node")
    doubly_linked_list.remove_head()
    doubly_linked_list.show()

    print("Remove Last Node")
    doubly_linked_list.remove_tail()
    doubly_linked_list.show()

    print("Linked list after removing a node:")
    doubly_linked_list.show()

    print("Size of linked list :", end=" ")
    print(doubly_linked_list.size())
