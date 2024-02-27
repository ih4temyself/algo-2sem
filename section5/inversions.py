def find_inversions(arr):
    inversions = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                inversions.append((arr[i], arr[j]))
    return inversions


if __name__ == "__main__":
    input_arr1 = [8, 4, 2, 1]
    input_arr2 = [1, 20, 6, 4, 5]

    print(find_inversions(input_arr1))
    print(find_inversions(input_arr2))