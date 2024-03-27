class ListNode:
    def __init__(self, key=None, val=None):
        self.key = key
        self.value = val
        self.next = None

    def __str__(self):
        if self.next is None:
            return f"{self.key}: {self.value}"

        return f"{self.key}: {self.value} -> {self.next}"


class MyHashTable:
    def __init__(self):
        self.slots = 10
        self.load_factor = 0.75
        self.hash_arr = [None] * self.slots
        self.number_of_taken_slots = 0

    def __str__(self):
        return "  |  ".join(map(str, self.hash_arr))

    def hash_function(self, key) -> int:
        return hash(key) % self.slots

    def put(self, key, value) -> ListNode:
        """
        :param key:
        :param value:
        :return:
        """
        if self.number_of_taken_slots / self.slots >= self.load_factor:
            self.rehashing()

        # if slot empty
        idx = self.hash_function(key)
        if self.hash_arr[idx] is None:
            self.hash_arr[idx] = ListNode(key, value)
            self.number_of_taken_slots += 1
            return self.hash_arr[idx]

        # if key exist
        curr_node = self.hash_arr[idx]
        while True:
            if curr_node.key == key:
                curr_node.value = value
                return curr_node
            if curr_node.next is None:
                break
            curr_node = curr_node.next

        # if key is new
        curr_node = self.hash_arr[idx]
        new_node = ListNode(key, value)
        new_node.next = curr_node
        self.hash_arr[idx] = new_node
        return self.hash_arr[idx]

    def get(self, key):
        """
        returns value by key. If result is not found return None
        :param key:
        :return:
        """
        idx = self.hash_function(key)
        if self.hash_arr[idx] is None:
            return None
        curr_node = self.hash_arr[idx]
        while curr_node:
            if curr_node.key == key:
                return curr_node.value
            curr_node = curr_node.next
        return None

    def remove(self, key):
        """
        returns key-value pair by key
        :param key:
        :return:
        """
        idx = self.hash_function(key)
        current_node = self.hash_arr[idx]
        previous_node = None
        while True:
            if current_node.key == key:
                if previous_node:
                    previous_node.next = current_node.next
                else:
                    self.hash_arr[idx] = current_node.next
                return
            if current_node.next is None:
                break
            previous_node = current_node
            current_node = current_node.next

    def rehashing(self):
        """
        increase the slots number if load factor is high.
        :return:
        """
        old_arr = self.hash_arr
        self.slots *= 2
        self.hash_arr = [None] * self.slots

        for node in old_arr:
            if node:
                idx = self.hash_function(node.key)
                self.hash_arr[idx] = node


if __name__ == "__main__":
    obj = MyHashTable()
    print(obj)
    obj.put("1", 1)
    obj.put("1", 2)
    obj.put("2", 27)
    obj.put("3", 12)
    obj.put("4", 2)
    obj.put("14", 22)
    obj.put("24", 2)
    obj.put("33", 8)
    obj.put("44", 1)
    obj.put("54", 1)
    obj.put("64", 2)
    obj.put("74", 3)
    obj.put("84", 247)
    obj.put("94", 6246)
    print(f"{obj}\n")
    obj.rehashing()
    print(f"{obj}\n")
    obj.put("o", 23)
    obj.put("a", 3)
    obj.put("d", 5)
    obj.put("c", 6)
    obj.put("v", 7)
    obj.put("b", 8)
    print(obj)

    # print(obj.get("1"))
    # print(obj.get("14"))
    # print(obj.get("24"))

    # obj.remove("1")
    # obj.remove("2")
    # obj.remove("14")
    # print(obj)
