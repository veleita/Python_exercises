from audioop import add


def add_element(lst, new_el):
    if new_el in lst:
        raise ValueError("This element was already in the list")
    else:
        lst.append(new_el)

nums = [2, 3, 4, 5]
try:
    add_element(nums, 1)
    print(nums)
except ValueError as RepeatedElement:
    print(RepeatedElement)
try:
    add_element(nums, 2)
    print(nums)
except ValueError as RepeatedElement:
    print(RepeatedElement)


def get_value_from_key(dict, key):
    if key not in dict:
        raise ValueError("The provided key doesn't exist in this dictionary")
    else:
        return dict[key]

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
try:
    print(get_value_from_key(car, "year"))
except ValueError as KeyNotFound:
    print(KeyNotFound)
try:
    print(get_value_from_key(car, "yea"))
except ValueError as KeyNotFound:
    print(KeyNotFound)