class Node:
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right


def array_to_tree(arr):

    def createNode(index):
        if index >= len(arr):
            return None

        node = Node(arr[index])
        node.left = createNode(2 * index + 1)
        node.right = createNode(2 * index + 2)

        return node

    return createNode(0)


if __name__ == "__main__":
    arr = [17, 0, -4, 3, 15]
    root = array_to_tree(arr)
