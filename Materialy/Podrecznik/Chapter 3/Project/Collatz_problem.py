def collatz(number):

    while number != 1:
        if number % 2 == 0:
            number = number // 2
            return number
        else:
            number = 3 * number + 1
            return number


input_number = int(input("Enter number"))

print(collatz(input_number))
