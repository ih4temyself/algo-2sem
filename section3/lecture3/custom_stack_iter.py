class Stack:
    def __init__(self):
        self._list = []

    def __str__(self):
        return str(self._list)

    def __iter__(self):
        """
        __iter__() returns the iterator object itself. If required, some initialization can be performed.
        """
        return self

    def __next__(self):
        """
        __next__() must return the next item in the sequence.
        On reaching the end, and in subsequent calls, it must raise StopIteration.
        """
        try:
            return self.pop()
        except IndexError:
            raise StopIteration

    def empty(self):
        """
        Returns whether the stack is empty – Time Complexity: O(1)
        :return:
        """
        return len(self._list) == 0

    def size(self):
        """
        Returns the size of the stack – Time Complexity: O(1)
        :return:
        """
        return len(self._list)

    def top(self):
        """
        Returns a reference to the topmost element of the stack – Time Complexity: O(1)
        :return:
        """
        return self._list[-1]

    def push(self, a):
        """
        Inserts the element ‘a’ at the top of the stack – Time Complexity: O(1)
        :return:
        """
        return self._list.append(a)

    def pop(self):
        """
        Deletes the topmost element of the stack – Time Complexity: O(1)
        :return:
        """
        return self._list.pop()


if __name__ == '__main__':
    s = Stack()
    s.push(3)
    s.push(8)
    s.push(9)
    s.push(8)
    s.push(9)
    s.push(8)
    s.push(9)
    s.pop()
    s.pop()
    s.push(10)
    s.pop()

    print(s)
    
    si = iter(s)
    print(next(si))
    print(next(si))
    print(next(si))

    print(s)

    for i in s:
        print(i)
