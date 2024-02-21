def bubble_sort(input_string, n):
    n = len(input_string)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if input_string[j] > input_string[j+1]:
                input_string[j], input_string[j+1] = input_string[j+1], input_string[j]
                swapped = True
        if not swapped:
            break