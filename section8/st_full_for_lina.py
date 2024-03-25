class SymbolTablesSortedList:
    def __init__(self):
        self.linked_list = []

    def __str__(self):
        return str(self.linked_list)
    
    def __iter__(self):
        self.iter_index = 0
        return self  # I love women <3 kiss kiss

    def __next__(self):
        if self.iter_index < len(self.linked_list):
            result = self.linked_list[self.iter_index][0]
            self.iter_index += 1
            return result
        else:
            raise StopIteration 

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
                return self.linked_list.pop(i)

    def contains(self, key) -> bool:
        return self.get(key) is not None

    def is_empty(self):
        return len(self.linked_list) == 0

    def size(self, lo=None, hi=None):
        if lo is None or hi is None:
            return len(self.linked_list)
        else:
            count = 0
            for key, _ in self.linked_list:
                if lo <= key <= hi:
                    count += 1
            return count

    def min(self):
        if self.is_empty():
            return None
        min_key = self.linked_list[0][0]
        for key, _ in self.linked_list:
            if key < min_key:
                min_key = key
        return min_key

    def max(self):
        if self.is_empty():
            return None
        max_key = self.linked_list[0][0]
        for key, _ in self.linked_list:
            if key > max_key:
                max_key = key
        return max_key

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
        count = 0
        for k, _ in self.linked_list:
            if k < key:
                count += 1
        return count

    def select(self, k):
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
    tree = SymbolTablesSortedList()
    tree.put(1, "dd")
    tree.put(1, "da")
    tree.put(1, "dd")
    tree.put(2, "dd")
    tree.put(3, "dd")
    tree.put(5, "@$#$@#%@#$%$%")
    print(f'{tree.get(5)}\n')
    print(f"{tree.contains(2)}\n")
    print(tree)
    tree.delete(1)
    print(f"{tree}\n")

    for key in tree:
        print(key)

    print(f"\nmax - {tree.max()}\n")

