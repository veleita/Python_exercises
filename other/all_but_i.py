# Given an array of integers, return a new array such that
# each element at index i of the new array is the product
# of all the numbers in the original array except the one at i

def all_but_i(integers):
    total = 1

    for i in integers:
        total *= i

    return [int(total / i) for i in integers]


def all_but_i_no_div(integers):
    total = 1

    for i in integers:
        total *= i

    return_list = []

    for i in integers:
        repeat = 1                  # This is just a way of dividing
        remainder = total           # using only subtractions
        while remainder > i:
            remainder -= i          # I did it because the challenge
            repeat += 1             # was solving this problem
        return_list.append(repeat)  # with no divisions

    return return_list


# TESTS
print(all_but_i([1, 2, 3, 4, 5]))   # [120, 60, 40, 30, 24]
print(all_but_i_no_div([1, 2, 3, 4, 5]))   # [120, 60, 40, 30, 24]

print(all_but_i([3, 2, 1]))         # [2, 3, 6]
print(all_but_i_no_div([3, 2, 1]))         # [2, 3, 6]
