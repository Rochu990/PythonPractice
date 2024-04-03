def gen(n):
    num = 0
    while num < n:
        yield num
        num += 1

for i, num in enumerate(gen(10)):
    print(i, num)