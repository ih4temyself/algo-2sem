class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def __eq__(self, other):
        return self.age == other.age and self.name == other.name

    def __hash__(self):
        print("The hash is:")
        return hash((self.age, self.name))


if __name__ == "__main__":
    person = Person(42, "Andrii")
    print(hash(person))
