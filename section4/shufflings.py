import random
from section4.random_lists_gen import custom_size_list_gen


# shuffle 1
def shuffle_with_dict(initial_list) -> list:
    random_numbers = {index: random.random() for index in range(len(initial_list))}
    shuffled_indices = sorted(random_numbers.keys(), key=lambda x: random_numbers[x])
    return [initial_list[i] for i in shuffled_indices]


# shuffle 2
def knuth_shuffle(ininitial_list) -> list:
    for i in range(len(ininitial_list) - 1):
        k = random.randint(0, len(ininitial_list) - 1)
        ininitial_list[i], ininitial_list[k] = ininitial_list[k], ininitial_list[i]
    return ininitial_list


# generation full shuffled list
def shuffled_list(size) -> list:
    return knuth_shuffle([random.randint(1, size) for _ in range(size)])


if __name__ == "__main__":
    small_list = custom_size_list_gen(100)
    medium_list = custom_size_list_gen(1000)
    large_list = custom_size_list_gen(10000)
    print(small_list)
    print(shuffle_with_dict(small_list))
    # print(shuffle_with_dict(medium_list))
    # print(shuffle_with_dict(large_list))

    # print(knuth_shuffle(small_list))
    # print(knuth_shuffle(medium_list))
    # print(knuth_shuffle(large_list))
