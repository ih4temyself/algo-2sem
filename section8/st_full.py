class STFull:
    def __init__(self):
        self.linked_list = []

    def __iter__(self):
        pass

    def __next__(self):
        pass  # I love women <3 kiss kiss

    def __str__(self):
        return str(self.linked_list)

    # you are also okay maybe

    def put(self, key, val) -> tuple:
        node = (key, val)
        for i in range(len(self.linked_list)):
            if self.linked_list[i][0] == key:
                self.linked_list[i] = node
                return node
        self.linked_list.append(node)
        return node

    def get(self, key):
        for i in self.linked_list:
            if i[0] == key:
                return i[1]
        return None

    def delete(self, key):
        for i in range(len(self.linked_list)):
            if key == self.linked_list[i][0]:
                el = self.linked_list[i]
                del self.linked_list[i]
                return el

    def contains(self, key) -> bool:
        if self.get(key) is None:
            return False
        return True

    def is_empty(self):
        pass

    def size(self, lo=None, hi=None):
        """
        should return the number of all keys if lo and hi are not passed.
        In other case, returns the number of keys between lo and hi
        :param lo:
        :param hi:
        :return:
        """
        pass

    def min(self):
        pass

    def max(self):
        pass

    def keys(self, lo=None, hi=None):
        """
        returns a list of all keys.
        If lo and hi are passed, returns a list of keys between lo and hi
        :param lo:
        :param hi:
        :return:
        """

    def floor(self, key):
        """
        найбільший ключ менший або рівний key
        :param key:
        :return:
        """
        pass

    def ceiling(self, key):
        """
        найменший ключ більший або рівний key
        :param key:
        :return:
        """
        pass

    def rank(self, key):
        """
        кількість ключів менших за key
        :param key:
        :return:
        """
        pass

    def select(self, k):
        pass

    def delete_min(self):
        pass

    def delete_max(self):
        pass


if __name__ == "__main__":
    my_table = STFull()
    my_table.put(1, "dd")
    my_table.put(1, "da")
    my_table.put(1, "dd")
    my_table.put(2, "dd")
    my_table.put(3, "dd")
    print(my_table.contains(2))
    print(my_table)
    my_table.delete(1)
    print(my_table)