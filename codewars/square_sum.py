INPUT_NUM = 23

number_pool = list(range(1, INPUT_NUM + 1))

# * setting max square via a while cycle, unoptimised!!!

list_max = max(number_pool) + max(number_pool) - 1
print(list_max)

possible_squares = []
for number in number_pool:
    possible_squares.append(number * number)
    if number * number >= list_max:
        break

possible_squares = possible_squares[1 : len(possible_squares) + 1]
print(possible_squares)

# * main loop

answers = []


def attempt() -> list:
    for elem in number_pool[:]:
        current_pool = number_pool[:]
        current_pool.remove(elem)

        answer = [elem]
        index = 0

        for _ in range(INPUT_NUM):
            for number in current_pool:
                if (answer[index] + number) in possible_squares:
                    answer.append(number)
                    current_pool.remove(number)
                    index += 1

        answers.append(answer)

        if len(answer) != INPUT_NUM:
            continue

        return answer


print(attempt())
