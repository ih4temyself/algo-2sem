def formatter(digit):
    if digit < 10:
        return f"0{digit}"
    else:
        return f"{digit}"


def make_readable(seconds):
    if seconds <= 59:
        return f"00:00:{formatter(seconds)}"

    elif seconds <= 3599:
        minutes = seconds // 60
        seconds = seconds % 60
        return f"00:{formatter(minutes)}:{formatter(seconds)}"
    else:
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds %= 60
        return f"{formatter(hours)}:{formatter(minutes)}:{formatter(seconds)}"


if __name__ == "__main__":
    print(make_readable(359999))
