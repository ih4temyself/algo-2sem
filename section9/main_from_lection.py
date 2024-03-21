class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def pre_order(node):
    if not node:
        return []
    return [node.data] + pre_order(node.left) + pre_order(node.right)


# In-order traversal
def in_order(node):
    return []


# Post-order traversal
def post_order(node):
    return []


if __name__ == "__main__":
    a = Node("a", Node("b"), Node("c", Node("d")))
    print(pre_order(a))
