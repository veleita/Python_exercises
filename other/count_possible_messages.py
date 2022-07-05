# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
# You can assume that the messages are decodable. For example, '001' is not allowed.

def transform_element(element, i):
    new_element = element.copy()
    new_element[i-1:i+1] = [new_element[i-1] * 10 + new_element[i]]
    return(new_element)

def decoder(digits):

    if len(digits) == 1:
        return 1

    table = []
    table.append(list(map(int, digits)))

    for element in table:
        print(table)
        for i in range(1, len(element)):
            if element[i] <= 7 and element[i - 1] <= 2:
                new_element = transform_element(element, i)
                if new_element not in table:
                    table.append(new_element)
                    print(new_element)
        print()

    print(table)
    return len(table)

# TESTS
print(decoder("1456"))   # [1 4 5 6], [14 5 6]                        : 2
print(decoder("1156"))   # [1 1 5 6], [11 5 6], [1 15 6]              : 3
print(decoder("1416"))   # [1 4 1 6], [14 1 6], [14 16], [1 4 16]     : 4
print(decoder("1116"))   # [1 1 1 6], [11 1 6], [11 16], [1 11 6]
                         # [1 1 16]                                    : 5
print(decoder("13116"))  # [1 3 1 1 6], [13 1 1 6], [13 11 6],
                         # [13 1 16], [1 3 11 6], [1 3 1 16]           : 6