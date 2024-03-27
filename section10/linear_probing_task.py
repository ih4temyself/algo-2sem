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


class MyHashTable:
    def __init__(self):
        self.slots = 10
        self.load_factor = 0.75
        self.hash_arr = [None] * self.slots

    def hash_function(self, key) -> int:
        return hash(key) % self.slots

    def put(self, key, value):
        """
        :param key:
        :param value:
        :return:
        """

    def get(self, key):
        """
        returns value by key. If result is not found return None
        :param key:
        :return:
        """

    def remove(self, key):
        """
        returns key-value pair by key
        :param key:
        :return:
        """

    def rehashing(self):
        """
        increase the slots number if load factor is high.
        :return:
        """
        pass


if __name__ == "__main__":
    # your testing is here
    pass
