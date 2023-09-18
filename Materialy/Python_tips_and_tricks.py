# source https://www.youtube.com/watch?v=qEr9iRX4K0o&list=PL10kQzxeRXWs2_frP8JVbLpHXeUUEBZMk&index=40&t=3s

from functools import reduce


# 1----------------------------------

# a = 10
# b = 20

# a,b = b,a

# print(a, b)

# 2------------------------------------

# numbers = [6, 12, 14, 4, 29, 39, 31, 22]

# largest = max(numbers)
# print(largest)

# smallest = min(numbers)
# print(smallest)

# 3--------------------------------------

# evens = [x for x in range(20) if x%2 == 0]
# print(evens)

# 4----------------------------------------

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
           11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def square(n):
    return n**2

def even(n):
    return n % 2 == 0

def multiply(x, y):
    return x * y

# squares = list(map(square, numbers))
# print(squares)

# squares = list(map(lambda x: x**2, numbers))
# print(squares)

# evens = list(filter(even, numbers))
# print(evens)

# evens = list(filter(lambda x: x%2 == 0, numbers))
# print(evens)

# product = reduce(multiply, numbers)
# print(product)

product = reduce(lambda x,y: x*y, numbers)
print(product)
