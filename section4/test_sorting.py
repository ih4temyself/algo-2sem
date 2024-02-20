import time, random_lists_gen, shufflings, add_logs
from sortings import InsertionSort, SelectionSort, ShellSort

def sort_time_counter(sorting_function, input_list, size):
    start_time = time.time()
    sorting_function(input_list, size)
    end_time = time.time()

    return end_time - start_time

def experimenting(sorting_function, custom_list_dict):
    results = {}
    for list_gen_func, size_tests_dict in custom_list_dict.items():
        results[list_gen_func.__name__] = {}
        for size, tests in size_tests_dict.items():
            results[list_gen_func.__name__][size] = []
            for _ in range(tests):
                time_taken = sort_time_counter(sorting_function, list_gen_func(size), size)
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

    add_logs.add_data_to_log(experimenting(InsertionSort.insertion_sort, custom_lists), 'insertion_sort')
    add_logs.add_data_to_log(experimenting(SelectionSort.selection_sort, custom_lists), 'selection_sort')
    add_logs.add_data_to_log(experimenting(ShellSort.shell_sort, custom_lists), 'shell_sort')
   
