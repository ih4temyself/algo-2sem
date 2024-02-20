import time, random_lists_gen, shufflings
from sortings import InsertionSort, SelectionSort, ShellSort

def sort_time_counter(sorting_function, input_list):
    start_time = time.time()
    sorting_function(input_list)
    end_time = time.time()
    # print(input_list)

    return end_time - start_time

def experimenting(sorting_function, custom_list_dict):
    results = {}
    for list_gen_func, size_tests_dict in custom_list_dict.items():
        results[list_gen_func.__name__] = {}
        for size, tests in size_tests_dict.items():
            results[list_gen_func.__name__][size] = []
            for i in range(tests):
                input_list = list_gen_func(size)
                time_taken = sort_time_counter(sorting_function, input_list)
                results[list_gen_func.__name__][size].append(time_taken)
    return results

if __name__ == "__main__":
    custom_lists = {
        random_lists_gen.custom_size_list_gen: {100: 5, 1000: 5, 10000: 5},
        shufflings.shuffled_list: {1000: 5},
        random_lists_gen.ordered_list: {1000: 5},
        random_lists_gen.almost_ordered_list: {1000: 5},
        random_lists_gen.reversed_ordered_list: {1000: 5},
        random_lists_gen.almost_identical_list: {1000: 5}
    }

    print(experimenting(InsertionSort.insertion_sort, custom_lists))

    # print(experimenting(InsertionSort.insertion_sort, random_lists_gen.custom_size_list_gen, 100, 5))
    # print(experimenting(InsertionSort.insertion_sort, random_lists_gen.custom_size_list_gen, 1000, 5))
    # print(experimenting(InsertionSort.insertion_sort, random_lists_gen.custom_size_list_gen, 10000, 5))

    # print(experimenting(InsertionSort.insertion_sort, shufflings.shuffled_list, 1000, 5))
    # print(experimenting(InsertionSort.insertion_sort, random_lists_gen.ordered_list, 1000, 5))
    # print(experimenting(InsertionSort.insertion_sort, random_lists_gen.almost_ordered_list, 1000, 5))
    # print(experimenting(InsertionSort.insertion_sort, random_lists_gen.reversed_ordered_list, 1000, 5))
    # print(experimenting(InsertionSort.insertion_sort, random_lists_gen.almost_identical_list, 1000, 5))