import random
from random_lists_gen import large_list_gen, medium_list_gen, small_list_gen

def knuth_shuffle(lst):
    for i in range(len(lst) - 1):
        k = random.randint(0, len(lst) - 1)
        lst[i], lst[k] = lst[k], lst[i]
    return lst

if __name__ == "__main__":
    small_list = small_list_gen()
    medium_list = medium_list_gen()
    large_list = large_list_gen()

    print(knuth_shuffle(small_list))
    print(knuth_shuffle(medium_list))
    print(knuth_shuffle(large_list))