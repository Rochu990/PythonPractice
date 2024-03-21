
def from_decimal_to_binary_converter(number):
    result = ''
    while number > 0:
        result = str(number % 2) + result
        number = number // 2
    return result


def from_binary_to_decimal_converter(number):
    number = str(number)
    p = len(number) - 1
    result = 0
    for i in number:
        if i == "1":
            result += 1 * 2**p
        p -= 1
    return result


print(from_decimal_to_binary_converter(8))










