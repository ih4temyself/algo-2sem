"""
13.04.24
@author: дьяконенко денис
"""

from min_heap import MinPQ


def time_simulate(k, times, n=None):
    n = len(times)
    pq = MinPQ()

    for i in range(min(n, k)):
        pq.insert(times[i])
    last_served_time = 0

    for i in range(min(n, k), n):
        earliest_free_time = pq.del_min()
        new_finish_time = earliest_free_time + times[i]
        pq.insert(new_finish_time)
        last_served_time = max(last_served_time, new_finish_time)

    while not pq.is_empty():
        last_served_time = pq.del_min()

    return last_served_time


if __name__ == "__main__":
    k = 2
    times_test_case1 = [3, 1, 1, 2, 3]
    print(time_simulate(k, times_test_case1))

    k = 3
    times_test_case2 = [1, 2, 3, 4, 5, 3, 1]
    print(time_simulate(k, times_test_case2))
