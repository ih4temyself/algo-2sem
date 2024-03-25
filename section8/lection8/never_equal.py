class NeverEqual:
    def __eq__(self, other):
        return False

    def __hash__(self):
        return id(self) >> 4


if __name__ == "__main__":
    x = NeverEqual()
    print(f"Hash of x: {hash(x)}")
    print(f"id of x: {id(x)}")
    print(f"id of x >>4: {id(x) >> 4}")
    print(f"Is x equal to itself? {x ==x}")
    print(f"Is never_equal in a set of itself? {x in set([x])}")
