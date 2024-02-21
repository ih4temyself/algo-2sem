import random, string

def custom_size_list_gen(size): 
    return [random.randint(1, size) for _ in range(size)]

def ordered_list(size): 
    return [i for i in range(size)]

def almost_ordered_list(size, swap_probability=0.1):
    almost_list = [i for i in range(size)]
    for i in range(size):
        if random.random() < swap_probability:
            j = random.randint(0, size - 1)
            almost_list[i], almost_list[j] = almost_list[j], almost_list[i]
    return almost_list

def reversed_ordered_list(size):
    return [i for i in range(size, 0, -1)]

def almost_identical_list(size, identical_probability=0.9):
    return[random.randint(0, 2) if random.random() < identical_probability else random.randint(0, 1000) for _ in range(size)]

def custom_size_string_list_gen(size):
    return [''.join(random.choices(string.ascii_letters, k=random.randint(1, size))) for _ in range(size)]
