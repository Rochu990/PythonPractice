from operator import truediv, mul, add, sub

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def calc(operator, x, y):
    operators = {"+": add, "-": subtract, "*": multiply, "/": divide}
    method = operators.get(operator)
    if method:
        return method(x, y)

    return None

def calculator():
    operation = None
    allowed_operations = ["+", "-", "*", "/"]
    while operation not in allowed_operations:  # Wymuszamy na użytkowniku
        operation = input(
            """
        Podaj operację jaką chcesz wykonać
        + dodawanie
        - odejmowanie
        * mnożenie
        / dzielenie
        """
        )

    x = float(input("Podaj pierwszą liczbę: "))
    y = float(input("Podaj drugą liczbę: "))
    try:
        result = calc(operation, x, y)
    except ZeroDivisionError:
        print("Nie można dzielić przez zero")
    else:
        print(result)





