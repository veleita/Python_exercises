# Given list, numbers, of natural numbers, and a natural number, aim, determine
# if any pair in the numbers list adds up to aim
from math import ceil


def adds_up(numbers, aim):
    numbers = sorted(numbers, reverse=True)
    trimmed_list = []
    for num in numbers:
        if num <= aim:
            trimmed_list = numbers[numbers.index(num):]
            break

    numbers = trimmed_list

    complements = [aim - num for num in numbers[:ceil(len(numbers) / 2)]]

    for num in numbers[ceil(len(numbers) / 2):]:
        for match in complements:
            if match == num:
                return True

    return False


print(adds_up([15, 30, 10, 89, 6, 3, 0, 11], 21))
