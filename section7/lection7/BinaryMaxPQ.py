class BinaryMaxPQ:
    def __init__(self):
        self._elements = []
        self._elements.append(None)
        self._capacity = 0

    def __str__(self):
        return str(self._elements)

    def _swim(self, k):
        while k > 1 and self._less(k // 2, k):
            self._exch(k, k // 2)
            k = k // 2

    def insert(self, value):
        self._elements.append(value)
        self._capacity += 1
        self._swim(self._capacity)

    def _sink(self, k):
        """
        :param k: element index
        :return:
        """
        while 2 * k <= self._capacity:
            j = 2 * k
            if j < self._capacity and self._less(j, j + 1):
                j += 1
            if not self._less(k, j):
                break
            self._exch(k, j)
            k = j

    def del_max(self):
        max_el = self._elements[1]
        self._exch(1, self._capacity)
        self._capacity -= 1
        self._sink(1)
        del self._elements[-1]
        return max_el

    def _exch(self, k, j):
        self._elements[k], self._elements[j] = self._elements[j], self._elements[k]

    def _less(self, i, j):
        return self._elements[i] < self._elements[j]


if __name__ == "__main__":
    bmpq = BinaryMaxPQ()
    bmpq.insert(5)
    bmpq.insert(10)
    bmpq.insert(7)
    bmpq.insert(1)
    bmpq.insert(11)
    print(bmpq)
    print(bmpq.del_max())
    print(bmpq)
    print(bmpq.del_max())
    print(bmpq)
    print(bmpq.del_max())
    print(bmpq)
    print(bmpq.del_max())
    print(bmpq)
