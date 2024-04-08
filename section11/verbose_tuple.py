from collections.abc import Sequence
from logging_mixin import LoggingMixin


class VerboseTuple(Sequence, LoggingMixin):
    def __init__(self, *args) -> None:
        self.mytuple = tuple(args)
        self.info(f"Create tuple with {self.mytuple}")

    def __str__(self) -> str:
        return "VerboseTuple" + str(self.mytuple)

    def __getitem__(self, item):
        self.info(f"Get item from position '{item}'")
        return self.mytuple[item]

    def __len__(self):
        self.info(f"Get length")
        return len(self.mytuple)

    def __setitem__(self, key, value):
        raise TypeError("ERROR -- VerboseTuple -- Item assignment is not allowed")


if __name__ == "__main__":
    vt1 = VerboseTuple()
    # INFO -- VerboseTuple -- Create tuple with (,)
    vt2 = VerboseTuple(1)
    # INFO -- VerboseTuple -- Create tuple with (1,)
    vt3 = VerboseTuple(1, 2, 3)
    # INFO -- VerboseTuple -- Create tuple with (1, 2, 3)
    vt3[2] = 2
    # ERROR -- VerboseTuple -- Item assignment is not allowed
    print(vt3[1])
    # INFO -- VerboseTuple -- Get item from position '1'
    # 2
    print(len(vt2))
    # INFO -- VerboseTuple -- Get length
    # 1
    print(vt3)
    # VerboseTuple(1, 2, 3)
