def up_array(arr):
    for i in range(len(arr)):
        if len(str(arr[i])) > 1:
            return "nil"
    a_string = "".join(arr)
    a_int = int(a_string)
    a_int += 1
    a_string = str(a_int)
    return list(map(int, a_string))


if __name__ == "__main__":
    lst1 = [9, 9, 9, 9]
    lst2 = [0, 1, 3, 7]
    print(up_array(lst1))
    print(up_array(lst2))
