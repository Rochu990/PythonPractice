from operator import truediv, mul, add, sub

def calculator():
    operation = None
    allowed_operations = ["+", "-", "*", "/"]
    while operation not in allowed_operations:
        operation = input(
        """
    Podaj operacje jaką chcesz wykonać
    + dodawania
    - odejmowanie
    * mnożenie
    / dzielenie
    """
    )

    x = float(input("Dodaj pierwszą liczbę: "))
    y = float(input("Dodaj drugą liczbę "))
    try:
        result = calc(operation, x, y)
    except ZeroDivisionError:
        print("Nie można dzielić przez zero")
    else:
        print(result)