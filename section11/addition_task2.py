"""
13.04.24
@author: дьяконенко денис
"""


def check_prefix(test_cases):
    results = []
    for numbers in test_cases:
        sorted_numbers = sorted(numbers)
        possible = True
        for i in range(len(sorted_numbers) - 1):
            if sorted_numbers[i + 1].startswith(sorted_numbers[i]):
                possible = False
                break
        if possible:
            results.append("YES")
        else:
            results.append("NO")
    return results


if __name__ == "__main__":
    test_cases = [
        ["911", "97625999", "91125426"],
        ["113", "12340", "123440", "12345", "98346"],
        ["22", "432324", "2260"],
    ]

    checked = check_prefix(test_cases)
    for state in checked:
        print(state)
