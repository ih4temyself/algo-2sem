from math import sqrt

PRIME_NUMS = [
    2,
    3,
    5,
    7,
    11,
    13,
    17,
    19,
    23,
    29,
    31,
    37,
    41,
    43,
    47,
    53,
    59,
    61,
    67,
    71,
    73,
    79,
    83,
    89,
    97,
]


def is_prime(num):
    if num <= 1:
        return False
    else:
        new_num = sqrt(num)
        new_del = 0
        for i in range(len(PRIME_NUMS)):
            if new_num >= PRIME_NUMS[i]:
                new_del = PRIME_NUMS[i]
                if num % new_del == 0:
                    return False
            else:
                break
        return True


if __name__ == "__main__":
    print(is_prime(-41))
