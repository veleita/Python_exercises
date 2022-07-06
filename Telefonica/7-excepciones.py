from audioop import add


def add_element(lst, new_el):
    if new_el in lst:
        raise ValueError("This element was already in the list")
    else:
        lst.append(new_el)

nums = [2, 3, 4, 5]
add_element(nums, 1)
print(nums)
add_element(nums, 5)
print(nums)

