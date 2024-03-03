def sorting_cstm_order(a1, a2):
    result = []
    counts = {}
    for num in a1:
        counts[num] = counts.get(num, 0) + 1
    print(counts)
    for num in a2:
        if num in counts:
            result.extend([num] * counts[num])
            del counts[num]

    for num in sorted(counts.keys()):
        result.extend([num] * counts[num])

    return result


if __name__ == "__main__":
    a1 = [2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8]
    a2 = [2, 1, 8, 3]
    print(sorting_cstm_order(a1, a2))

    a1 = [4, 5, 1, 1, 3, 2]
    a2 = [3, 1]
