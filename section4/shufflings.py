import random 
from random_lists_gen import large_list_gen, medium_list_gen, small_list_gen

#shuffle 1
def dict_generator(initial_list): 
    return {element: random.random() for element in initial_list}

def sort_by_value(dictionary):
    return sorted(dictionary.keys(), key = lambda x: dictionary[x])

#shuffle 2 
def knuth_shuffle(ininitial_list):
    for i in range(len(ininitial_list) - 1):
        k = random.randint(0, len(ininitial_list) - 1)
        ininitial_list[i], ininitial_list[k] = ininitial_list[k], ininitial_list[i]
    return ininitial_list

if __name__ == "__main__":
    small_list = small_list_gen()
    medium_list = medium_list_gen()
    large_list = large_list_gen()

    small_dict = {}
    print(sort_by_value(dict_generator(small_list)))
    medium_dict= {}
    print(sort_by_value(dict_generator(medium_list)))
    large_dict= {}
    print(sort_by_value(dict_generator(large_list)))

    print(knuth_shuffle(small_list))
    print(knuth_shuffle(medium_list))
    print(knuth_shuffle(large_list))