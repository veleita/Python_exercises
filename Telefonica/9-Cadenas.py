def last_two(str):
    return str[-2:]

def last_three(str):
    return str[-3:]

def step_two(str):
    return str[::2]

def invert(str):
    return str[::-1]

def is_substr(str1, str2):
    if str1.find(str2) != -1:
        return True
    else:
        return False

def which_is_first(str1, str2):
    if str1 <= str2:
        return str1
    else:
        return str2


print(last_two("Arizona"))
print(last_three("Arizona"))
print(step_two("Arizona"))
print(invert("Arizona"))
print(is_substr("Arizona", "ona"))
print(is_substr("Arizona", "ola"))
print(which_is_first("Arizona", "Beluga"))
print(which_is_first("Arizona", "Arizono"))
print(which_is_first("Arizona", "A"))