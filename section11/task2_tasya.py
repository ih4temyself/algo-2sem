def has_prefix(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j and numbers[j].startswith(numbers[i]):
                return "YES"
    return "NO"


if __name__ == "__main__":
    test1 = ["911", "97625999", "91125426"]
    test2 = ["113", "12340", "123440", "12345", "9836"]
    print(has_prefix(test1))
    print(has_prefix(test2))
