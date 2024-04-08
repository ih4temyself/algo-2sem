"""
30.03.24
@author: дьяконенко денис

   "           ""#                                       ""#
 mmm             #     mmm   m   m   mmm           mmm     #     mmmm   mmm
   #             #    #" "#  "m m"  #"  #         "   #    #    #" "#  #" "#
   #             #    #   #   #m#   # " "         m" "#    #    #   #  #   #
 mm#mm           "mm  "#m#"    #    "#mm"         "mm"#    "mm  "#m"#  "#m#"
                                                                 m  #
"""


class MyHashTable:
    def __init__(self):
        self.slots = 10
        self.load_factor = 0.75
        self.hash_arr = [None] * self.slots
        self.load_state = 0

    def __str__(self):
        return str(self.hash_arr)

    def hash_function(self, key) -> int:
        return hash(key) % self.slots

    def put(self, key, value):
        """
        :param key:
        :param value:
        :return:
        """
        idx = self.hash_function(key)
        state_idx = idx
        while self.hash_arr[idx] is not None:
            if self.hash_arr[idx][0] == key:
                self.hash_arr[idx] = (key, value)
                return
            idx = (idx + 1) % self.slots
            if idx == state_idx:
                return

        if self._load_calculator():
            self.rehashing()
            self.put(key, value)
        else:
            self.hash_arr[idx] = (key, value)
            self.load_state += 1

    def get(self, key):
        """
        returns value by key. If result is not found return None
        :param key:
        :return:
        """
        idx = self.hash_function(key)
        state_idx = idx
        while self.hash_arr[idx] is not None:
            if self.hash_arr[idx][0] == key:
                return self.hash_arr[idx][1]
            idx = (idx + 1) % self.slots
            if idx == state_idx:
                return None

    def remove(self, key):
        """
        returns key-value pair by key
        :param key:
        :return:
        """
        idx = self.hash_function(key)
        state_idx = idx

        while self.hash_arr[idx] is not None:
            if self.hash_arr[idx][0] == key:
                removed_value = self.hash_arr[idx]
                self.hash_arr[idx] = None
                self.load_state -= 1

                next_idx = (idx + 1) % self.slots
                while self.hash_arr[next_idx] is not None:
                    rehash_key, rehash_val = self.hash_arr[next_idx]
                    self.hash_arr[next_idx] = None
                    self.load_state -= 1
                    self.put(rehash_key, rehash_val)
                    next_idx = (next_idx + 1) % self.slots

                return removed_value

            idx = (idx + 1) % self.slots
            if idx == state_idx:
                break
        return None

    def rehashing(self):
        """
        increase the slots number if load factor is high.
        :return:
        """
        old_arr = self.hash_arr
        self.slots *= 2
        self.hash_arr = [None] * self.slots
        for tup in old_arr:
            if tup:
                self.put(tup[0], tup[1])

    def _load_calculator(self):
        return self.load_state / self.slots >= self.load_factor


if __name__ == "__main__":
    # your testing is here
    ln_hashtable = MyHashTable()
    ln_hashtable.put("12", "j")
    ln_hashtable.put("13", "hlp")
    ln_hashtable.put("14", "jk")
    ln_hashtable.put("15", "k")
    ln_hashtable.put("16", "pls")
    ln_hashtable.put("17", "o")
    ln_hashtable.put("18", "m")
    ln_hashtable.put("19", "?")
    print(ln_hashtable)

    print(ln_hashtable.get("13"))
    print(ln_hashtable.get("16"))

    ln_hashtable.remove("14")
    print(ln_hashtable)
    ln_hashtable.put("14", "aa")

    print(f"\nrehash test\n")
    print(ln_hashtable)
    ln_hashtable.put("20", "rehash")  # rehashing moment
    print(ln_hashtable.get("20"))
    print(ln_hashtable)
