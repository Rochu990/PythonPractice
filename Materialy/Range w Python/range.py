# source: https://ddeby.pl/blog/range-w-python

print([a for a in range(10)])

print([a for a in range(5, 10)])

print([a for a in range(1, 10, 2)])

print([a for a in range(5, 0, -1)])


def table(n):
    for i in range(n):
        print([j for j in range(n)])


print(table(10))
