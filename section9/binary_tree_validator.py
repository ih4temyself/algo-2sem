"""
22.03.24
@author: дьяконенко денис
 mmmmm   mmm    mmm  m     m
 # # #  #"  #  #" "# "m m m"
 # # #  # ""   #   #  #m#m#
 # # #  "#mm"  "#m#"   # #
"""


class T:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def _in_order(node):
    if not node:
        return []
    return _in_order(node.left) + [node.value] + _in_order(node.right)


def is_bst(node) -> bool:
    mytree = _in_order(node)
    return (
        True
        if mytree == sorted(mytree) or mytree == sorted(mytree, reverse=True)
        else False
    )


if __name__ == "__main__":
    test1 = T(5, T(2, T(1), T(3)), T(7, None, T(9)))
    test2 = T(6, T(1, None, T(7)), T(10))  # my test
    test3 = T(7, T(9), T(2))  # test from codewars
    test4 = T(5, None, T(4))  # test from codewars
    print(is_bst(test1))
    print(is_bst(test2))
    print(is_bst(test3))
    print(is_bst(test4))
