# Given an array of integers, find the first missing positive integer.
# In other words, find the lowest positive integer that does not exist in the array.
# The array can contain duplicates and negative numbers as well.

def find_first_missing(integers):
    missing = max(integers) + 1

    integers = sorted(integers)
    for i in integers:
        if i != max(integers) and integers[integers.index(i) + 1] != i + 1 and i + 1 != 0:
            missing = i + 1
            break
    return missing


# TESTS
print(find_first_missing([3, 4, -1, 1]))    # Should give 2
print(find_first_missing([1, 2, 0]))        # Should give 3