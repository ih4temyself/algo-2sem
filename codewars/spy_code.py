from itertools import product


def get_pins(observed):
    adjacent_digits = {
        "0": ["0", "8"],
        "1": ["1", "2", "4"],
        "2": ["1", "2", "3", "5"],
        "3": ["2", "3", "6"],
        "4": ["1", "4", "5", "7"],
        "5": ["2", "4", "5", "6", "8"],
        "6": ["3", "5", "6", "9"],
        "7": ["4", "7", "8"],
        "8": ["5", "7", "8", "9", "0"],
        "9": ["6", "8", "9"],
    }

    variations = [adjacent_digits[digit] for digit in observed]
    possible_pins = ["".join(pin) for pin in product(*variations)]

    return possible_pins


if __name__ == "__main__":
    print(get_pins(["5", "7", "8", "9", "0"]))
