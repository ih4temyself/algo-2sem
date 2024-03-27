"""
27.03.24
@author: дьяконенко денис

   "           ""#                                       ""#
 mmm             #     mmm   m   m   mmm           mmm     #     mmmm   mmm
   #             #    #" "#  "m m"  #"  #         "   #    #    #" "#  #" "#
   #             #    #   #   #m#   # " "         m" "#    #    #   #  #   #
 mm#mm           "mm  "#m#"    #    "#mm"         "mm"#    "mm  "#m"#  "#m#"
                                                                 m  #
"""


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def max_sum(root: TreeNode) -> int:
    if not root:
        return 0

    def find_max(root):
        if root is None:
            return float("-inf")  # aaaaaa aaa aa a a a a a a a a a a a aaaaaaa
        if root.left is None and root.right is None:
            return root.value

        left_sum = find_max(root.left)
        right_sum = find_max(root.right)

        return root.value + max(left_sum, right_sum)

    return find_max(root)


if __name__ == "__main__":
    root = TreeNode(
        17,
        TreeNode(3, TreeNode(2)),
        TreeNode(-10, TreeNode(16), TreeNode(1, TreeNode(13))),
    )
    print(max_sum(root))  # output: 23 like in example
