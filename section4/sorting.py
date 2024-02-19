from random_lists_gen import small_list_gen, medium_list_gen, large_list_gen

def selection_sort(ininitial_list): 
    for i in range(len(ininitial_list)):
        min_id = i
        for j in range(i+1, len(ininitial_list)):
            if ininitial_list[j] < ininitial_list[min_id]:
                min_id = j 
        ininitial_list[i], ininitial_list[min_id] = ininitial_list[min_id], ininitial_list[i]
    return ininitial_list

def insertion_sort(initial_list):
    for i in range(1, len(initial_list)): 
        key = initial_list[i]
        j = i - 1
        while j >= 0 and initial_list[i] < initial_list[j]:
            initial_list[j + 1] = initial_list[j]
            j -= 1
        initial_list[j+1] = key

if __name__ == "__main__":
    small_list = small_list_gen()
    medium_list = medium_list_gen()
    large_list = large_list_gen() 

    print(len(small_list))
    print(selection_sort(small_list))