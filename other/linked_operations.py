# Define a series of functions, one for each decimal number and one for each basic mathematical operation
# so that the operations can be performed as follows:
#   seven(times(five()) == 35
#   eight(minus(nine()) == -1

def zero(operation=None): return operation(0) if operation else 0
def one(operation=None): return 1 if not operation else operation(1)
def two(operation=None): return operation(2) if operation else 2
def three(operation=None): return operation(3) if operation else 3
def four(operation=None): return operation(4) if operation else 4
def five(operation=None): return operation(5) if operation else 5
def six(operation=None): return operation(6) if operation else 6
def seven(operation=None): return operation(7) if operation else 7
def eight(operation=None): return operation(8) if operation else 8
def nine(operation=None): return operation(9) if operation else 9


def plus(num2): return lambda num1: num1 + num2
def minus(num2): return lambda num1: num1 - num2
def times(num2): return lambda num1: num1 * num2
def divided_by(num2): return lambda num1: num1 / num2
def module(num2): return lambda num1: num1 % num2


# TESTS
print(seven(plus(eight())))                 # 7 + 8 = 15
print(one(minus(four())))                   # 1 - 4 = -3
print(five(times(five())))                  # 5 * 5 = 25
print(six(divided_by(two())))               # 6 / 2 = 3
print(eight(module(three())))               # 8 % 3 = 2
print(six(plus(four(divided_by(two())))))   # 6 + 4 / 2 = 8
