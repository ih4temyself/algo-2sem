import random 

def small_list_gen(): 
    return [random.randint(1, 100) for _ in range (100)]

def medium_list_gen():
    return [random.randint(1, 1000) for _ in range(1000)]

def large_list_gen():
    return [random.randint(1, 10000) for _ in range (10000)]
