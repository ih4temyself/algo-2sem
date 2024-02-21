import time
import random_lists_gen, shufflings, add_logs
from sortings import InsertionSort, SelectionSort, ShellSort, BubbleSort

class Experiment:
    def __init__(self, list_generator, sizes, iterations):
        self.list_generator = list_generator
        self.sizes = sizes
        self.iterations = iterations

    def run(self, sorting_function):
        results = {}
        for size in self.sizes:
            results[size] = []
            for _ in range(self.iterations):
                input_list = self.list_generator(size)
                start_time = time.time()
                sorting_function(input_list, size)
                end_time = time.time()
                time_taken = end_time - start_time
                results[size].append(time_taken)
        return results

if __name__ == "__main__":
    experiments = [
        Experiment(random_lists_gen.custom_size_list_gen, [100, 1000, 10000], 5),
        Experiment(shufflings.shuffled_list, [1000], 5),
        Experiment(random_lists_gen.ordered_list, [1000], 5),
        Experiment(random_lists_gen.almost_ordered_list, [1000], 5),
        Experiment(random_lists_gen.reversed_ordered_list, [1000], 5),
        Experiment(random_lists_gen.almost_identical_list, [1000], 5,),
        Experiment(random_lists_gen.custom_size_string_list_gen, [1000,1000], 5)
    ]

    sorting_algorithms = {
        'InsertionSort': InsertionSort.insertion_sort,
        'SelectionSort': SelectionSort.selection_sort,
        'ShellSort': ShellSort.shell_sort,
        'BubbleSort': BubbleSort.bubble_sort
    }

    for algorithm_name, sorting_function in sorting_algorithms.items():
        results = {}
        for experiment in experiments:
            results[experiment.list_generator.__name__] = experiment.run(sorting_function)
        add_logs.add_data_to_log(results, algorithm_name)