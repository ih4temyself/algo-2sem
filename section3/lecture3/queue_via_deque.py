from collections import deque


def queue_test():
    my_queue = deque()
    my_queue.append(5)
    my_queue.append(6)
    my_queue.append(9)

    my_queue.popleft()

    my_queue.append(7)
    my_queue.popleft()

    print(my_queue)

    for i in my_queue:
        print(i)


if __name__ == "__main__":
    queue_test()
