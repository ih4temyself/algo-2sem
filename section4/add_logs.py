import os, re


def add_data_to_log(data_dict, sort_label):
    next_number = 1
    while os.path.exists(f"section4/logs/log-{sort_label}-{next_number}.txt"):
        next_number += 1

    with open(f"section4/logs/log-{sort_label}-{next_number}.txt", "w") as file:
        file.write(f"·:*¨༺ ♱✮♱ ༻¨*:·\n")
        file.write(f"  ╱|、\n(˚ˎ 。7  \n |、˜〵  \nじしˍ,)ノ:·\n\n")

        flattened_data = []
        for key, value in data_dict.items():
            for size, times in value.items():
                avg_time = sum(times) / len(times)
                flattened_data.append((key, size, avg_time, times))

        # Sort the data based on the average time
        sorted_data = sorted(flattened_data, key=lambda x: x[2])

        # Write the sorted data into the text file
        for key, size, avg_time, experiments in sorted_data:
            file.write(f"૮₍ ˃ ⤙ ˂ ₎ა¨*:·\n")
            file.write(f"{key} - size: {size}, average Time: {avg_time}\n")
            file.write("experiments:\n")
            for i, time in enumerate(experiments, 1):
                file.write(f"experiment {i}: {time}\n")
            file.write(f"·:*¨༺ ♱✮♱ ༻¨*:·\n\n")


if __name__ == "__main__":
    # add_data_to_log(data1, 'section4/logs.txt')
    pass
