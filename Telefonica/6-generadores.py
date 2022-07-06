def generate_even_nums():
    num = 1
    while True:
        yield num * 2
        num += 1

# Commented because they cannot be tested at the same time
#gen_2 = generate_even_nums()
#for n in gen_2:
#    print(n)


def generate_3_multiple():
    num = 1
    while True:
        yield num * 3
        num += 1

gen_3 = generate_3_multiple()
for n in gen_3:
    print(n)