import time


def square_sums(target_num: int) -> list:
    number_pool = list(range(1, target_num + 1))
    list_max = max(number_pool) + max(number_pool) - 1

    possible_squares = []
    for number in number_pool:
        possible_squares.append(number**2)
        if number**2 >= list_max:
            break

    def find_sequence(current_pool, current_sequence):
        if len(current_sequence) == target_num:
            return current_sequence
        for number in current_pool:
            if (
                not current_sequence
                or (current_sequence[-1] + number) in possible_squares
            ):
                next_pool = current_pool[:]
                next_pool.remove(number)
                next_sequence = current_sequence + [number]
                result = find_sequence(next_pool, next_sequence)
                if result:
                    return result
        return None

    for start_num in number_pool:
        sequence = find_sequence(number_pool[:], [start_num])
        if sequence:
            return sequence

    return False


if __name__ == "__main__":
    start_time = time.time()
    print(square_sums(15))
    end_time = time.time()
    time_taken = end_time - start_time
    print(time_taken)
