def move_zeros(lst):
    output_lst = []
    zero_counter = 0

    for i in range(len(lst)):
        if lst[i] != 0:
            output_lst.append(lst[i])
        else:
            zero_counter += 1

    for _ in range(zero_counter):
        output_lst.append(0)
    return output_lst


if __name__ == "__main__":
    print(move_zeros([1, 0, 1, 2, 0, 1, 3]))
