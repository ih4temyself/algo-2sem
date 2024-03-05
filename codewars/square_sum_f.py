import time


def attempt(target_num: int) -> list:
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
            return [target_num, possible_squares, sequence]

    return False


def attempt_optimized(target_num: int):
    # Generate the pool of numbers and possible squares more efficiently
    number_pool = set(range(1, target_num + 1))
    list_max = 2 * target_num - 1

    possible_squares = {i**2 for i in range(1, int(list_max**0.5) + 1)}

    # Memoization cache
    cache = {}

    def find_sequence(current_pool, current_sequence):
        # Check if current state is in cache
        current_state = tuple(current_sequence)
        if current_state in cache:
            return cache[current_state]

        if len(current_sequence) == target_num:
            return current_sequence
        for number in sorted(current_pool):  # Sort to try lower numbers first
            if (
                not current_sequence
                or (current_sequence[-1] + number) in possible_squares
            ):
                next_pool = current_pool.copy()
                next_pool.remove(number)
                next_sequence = current_sequence + [number]
                result = find_sequence(next_pool, next_sequence)
                if result:
                    cache[current_state] = result
                    return result

        # Cache the failure state to avoid re-computation
        cache[current_state] = None
        return None

    for start_num in number_pool:
        sequence = find_sequence(number_pool - {start_num}, [start_num])
        if sequence:
            return [target_num, sorted(possible_squares), sequence]

    return False


if __name__ == "__main__":
    start_time = time.time()
    print(attempt(49))
    end_time = time.time()
    time_taken = end_time - start_time
    print(time_taken)

    start_time = time.time()
    print(attempt_optimized(49))
    end_time = time.time()
    time_taken = end_time - start_time
    print(time_taken)
