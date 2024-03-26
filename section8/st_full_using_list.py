class SymbolTablesSortedList:
    def __init__(self):
        self.linked_list = []
        self.iter_index = 0  # for iteration

    def __iter__(self):
        self.iter_index = 0
        return self

    def __next__(self):
        if self.iter_index < len(self.linked_list):
            result = self.linked_list[self.iter_index][0]
            self.iter_index += 1
            return result
        else:
            raise StopIteration

    def __str__(self):
        return str(self.linked_list)

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

    def delete(self, key):  # changed and it works
        for i in range(len(self.linked_list)):
            if key == self.linked_list[i][0]:
                return self.linked_list.pop(i)

    def contains(self, key) -> bool:
        return self.get(key) is not None

    def is_empty(self) -> bool:
        return len(self.linked_list) == 0

    def size(self, lo=None, hi=None):
        if lo is None or hi is None:
            return len(self.linked_list)
        else:
            return len([key for key, _ in self.linked_list if lo <= key <= hi])

    def min(self):
        if self.is_empty():
            return None
        return min(self.linked_list, key=lambda x: x[0])[0]

    def max(self):  # finds max key, iterates via keys <3
        if self.is_empty():
            return None
        return max(self.linked_list, key=lambda x: x[0])[0]

    def keys(self, lo=None, hi=None):
        if lo is None or hi is None:
            return [key for key, _ in self.linked_list]
        else:
            return [key for key, _ in self.linked_list if lo <= key <= hi]

    def floor(self, key):
        keys_less_than_equal = [k for k, _ in self.linked_list if k <= key]
        return max(keys_less_than_equal) if keys_less_than_equal else None

    def ceiling(self, key):
        keys_greater_than_equal = [k for k, _ in self.linked_list if k >= key]
        return min(keys_greater_than_equal) if keys_greater_than_equal else None

    def rank(self, key):
        return len([k for k, _ in self.linked_list if k < key])

    def select(self, k):  # selects key with index (?)??
        if k < 0 or k >= len(self.linked_list):
            return None
        return sorted(self.linked_list, key=lambda x: x[0])[k][0]

    def delete_min(self):
        if self.is_empty():
            return None
        min_key = self.min()
        return self.delete(min_key)

    def delete_max(self):
        if self.is_empty():
            return None
        max_key = self.max()
        return self.delete(max_key)


if __name__ == "__main__":
    my_table = SymbolTablesSortedList()
    my_table.put(1, "help")
    print(my_table)
    my_table.put(1, "changed")
    print(my_table)
    my_table.put(1, "again")
    my_table.put(2, "lll")
    my_table.put(3, "<3")
    my_table.put(4, "3")

    print(my_table.contains(2))
    print(my_table)

    my_table.delete(1)
    print(my_table)

    print(my_table.size(0, 4))
    print(my_table.max())

    print(f"\niterate via list")
    for obj in my_table:
        print(f"{obj}:{my_table.get(obj)}")

    print(my_table.rank(4))  # 2 keys smaller than 4 so it works eeii

    my_table.delete_max()
    print(my_table)  # deleted key 4 so works
