import random 
from random_lists_gen import large_list_gen, medium_list_gen, small_list_gen

def dict_generator(lst): 
    return {element: random.random() for element in lst}

def sort_by_value(dictionary):
    return sorted(dictionary.keys(), key = lambda x: dictionary[x])

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