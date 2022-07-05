# cons(a, b) constructs a pair given the following implementation

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

# car(pair) and cdr(pair) returns the first and last element of that pair.
# Implement car and cdr


def car(pair):
    pass


def cdr(pair):
    pass


car(cons(3, 4))
cdr(cons(3, 4))
