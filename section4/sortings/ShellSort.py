def shell_sort(array, n):
    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    interval = n // 2

    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp

        interval //= 2


if __name__ == "__main__":
    data = [9, 8, 3, 7, 5, 6, 4, 1]
    size = len(data)
    shell_sort(data, size)
    print("Sorted Array in Ascending Order:")
    print(data)
