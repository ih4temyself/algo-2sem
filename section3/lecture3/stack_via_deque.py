from collections import deque


def stack_test():
    my_stack = deque()
    my_stack.append(5)
    my_stack.append(6)
    my_stack.append(9)

    my_stack.pop()

    my_stack.append(7)
    my_stack.pop()

    print(my_stack)


if __name__ == "__main__":
    stack_test()
